from odoo import api, fields, models, _
from datetime import date

class Custody(models.Model):
    _name = 'custody'
    _description = 'Custody'
    _rec_name = 'sequence_number'
    _inherit = 'mail.thread'

    sequence_number = fields.Char(
        string='Number',
        copy=False,
        readonly=True,
        default=lambda self: self.env['ir.sequence'].next_by_code('custody')
    )
    property_type = fields.Many2one('custody.property.type', string='Type')
    property_id = fields.Many2one('custody.property', string="Property", tracking=True, required=True,
                                  domain="[('property_type', '=?', property_type)]")
    employee_id = fields.Many2one('hr.employee', string='Employee', ondelete='cascade', required=True)
    model_number = fields.Char(related='property_id.model_number', string="Model Number", tracking=True)
    state = fields.Selection(
        selection=[('draft', 'Draft'), ('issued', 'Issued'), ('withdraw', 'Withdraw')],
        string='Status',
        default='draft',
        tracking=True
    )
    date_of_issue = fields.Date(string='Issued Date', default=lambda self: date.today(), tracking=True)
    return_date = fields.Date(string='Return Date', readonly=True, tracking=True)
    note = fields.Html(string='Notes')
    resignation_id = fields.Many2one('employee.resignation', string="Resignation")

    @api.constrains('property_id', 'return_date')
    def _check_unique_property(self):
        for record in self:
            if record and self.search_count([
                ('property_id', '=', record.property_id.id),
                ('id', '!=', record.id),
                ('return_date', '=', None)
            ]):
                raise models.ValidationError(_('This property is already assigned to another employee.!!!'))

    def button_state_change(self):
        for record in self:
            # Check if the property is already assigned to another active custody record
            if self.search_count([
                ('property_id', '=', record.property_id.id),
                ('id', '!=', record.id),
                ('return_date', '=', None)
            ]):
                raise models.ValidationError(_('This property is already assigned to another employee.'))
            record.state = 'issued'

    def action_return_date(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Return Date'),
            'res_model': 'property.return.date.wizard',
            'target': 'new',
            'view_mode': 'form',
            'context': {'default_custody_id': self.id},
        }

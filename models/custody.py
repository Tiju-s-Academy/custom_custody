from odoo import fields, models,_

class Custody(models.Model):
    _name = 'custody'
    _description = 'Custody'
    _rec_name = 'sequence_number'
    _inherit = 'mail.thread'
    _sql_constraints = [('property_id_unique', 'unique(property_id)', 'This property is '
                                                                      'already Assigned a another employee')]

    sequence_number = fields.Char(string='Number', copy=False, readonly=True,
                                  default=lambda self: self.env['ir.sequence'].next_by_code('custody'))
    property_id = fields.Many2one('custody.property', string="Property")
    employee_id = fields.Many2one('hr.employee', string='Employee', ondelete='cascade')
    model_number = fields.Char(related='property_id.model_number', string="Model Number")
    state = fields.Selection(selection=[('draft', 'Draft'), ('issued', 'Issued'), ('withdraw', 'withdraw')],
                             string='Status', default='draft', tracking=True)
    date_of_issue = fields.Date(string='Issued Date')
    return_date = fields.Date(string='Return Date', readonly=True)
    note = fields.Html(string='notes')

    def button_state_change(self):
        self.state = 'issued'

    def action_return_date(self):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Return Date'),
            'res_model': 'property.return.date.wizard',
            'target': 'new',
            'view_mode': 'form',
            'context': {'default_custody_id': self.id},
        }







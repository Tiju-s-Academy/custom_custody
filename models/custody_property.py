from odoo import api,fields,models


class CustodyProperty(models.Model):
    _name = 'custody.property'
    _desc = 'Custody Property'

    _inherit = 'mail.thread'

    number = fields.Char(string="ID")
    name = fields.Char(string='Name')
    model_number = fields.Char(string="Model Number")
    property_type = fields.Many2one('custody.property.type',string='Type')
    purchase_rate = fields.Date(string='Purchase Date')
    estimated_value = fields.Float(string='estimated Value')
    note = fields.Html(string='note')

    custody_employee_log = fields.Html(string='Employee Log', compute='_compute_custody_log', store=False)

    @api.depends('name')
    def _compute_custody_log(self):
        for property_rec in self:
            log_entries = self.env['custody'].search([('property_id', '=', property_rec.id)],
                                                     order='date_of_issue desc')
            history = ""
            for entry in log_entries:
                history += f"""
                   <p>
                       <strong>Employee:</strong> {entry.employee_id.name}<br/>
                       <strong>Issued Date:</strong> {entry.date_of_issue}<br/>
                       <strong>Return Date:</strong> {entry.return_date or 'Still In Use'}<br/>
                       <strong>State:</strong> {entry.state}
                   </p>
                   <hr/>
                   """
            property_rec.custody_employee_log = history


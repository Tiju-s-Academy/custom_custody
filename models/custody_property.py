from odoo import fields,models


class CustodyProperty(models.Model):
    _name = 'custody.property'
    _desc = 'Custody Property'
    _sql_constraints = [('number_unique', 'unique(number)', 'This numbers is already used in another Products')]
    _inherit = 'mail.thread'

    number = fields.Char(string="ID")
    name = fields.Char(string='Name')
    model_number = fields.Char(string="Model Number")
    property_type = fields.Many2one('custody.property.type',string='Type')
    purchase_rate = fields.Date(string='Purchase Date')
    estimated_value = fields.Float(string='estimated Value')
    note = fields.Html(string='note')

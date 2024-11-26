from odoo import fields, models


class CustodyPropertyType(models.Model):
    _name = 'custody.property.type'

    name = fields.Char(string='Name')

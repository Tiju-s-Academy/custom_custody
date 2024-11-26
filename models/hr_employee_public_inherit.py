from odoo import fields,models


class HrEmployeePublicInherit(models.Model):
    _inherit = 'hr.employee.public'

    custody_ids = fields.One2many('custody', 'employee_id', string="Custody Records")
    custody_count = fields.Integer(string='Custody Count', compute='_compute_custody_count')

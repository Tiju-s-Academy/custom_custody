from odoo import fields, models


class HrEmployeeInherit(models.Model):
    _inherit = 'hr.employee'

    custody_ids = fields.One2many('custody', 'employee_id', string="Custody Records", ondelete='cascade')
    custody_count = fields.Integer(string='Custody Count', compute='_compute_custody_count')

    def action_view_custody(self):
        self.ensure_one()
        return {
            'name': 'Custody Records',
            'type': 'ir.actions.act_window',
            'res_model': 'custody',
            'view_mode': 'tree,form',
            'domain': [('employee_id', '=', self.id)],
            'context': {'default_employee_id': self.id},
        }

    def _compute_custody_count(self):
        for employee in self:
            employee.custody_count = self.env['custody'].search_count([('employee_id', '=', employee.id)])




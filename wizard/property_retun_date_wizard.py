from odoo import fields, models


class PropertyReturnDateWizard(models.TransientModel):
    _name = 'property.return.date.wizard'

    return_date = fields.Date(string='Return Date',required=True)
    custody_id = fields.Many2one('custody',string='custody', readonly=True)

    def action_submit_return_date(self):
        if self.custody_id:
            # Write the hold_date to the Approval Request's hold_date field
            self.custody_id.write({
                'return_date': self.return_date,
                'state': 'withdraw',
            })



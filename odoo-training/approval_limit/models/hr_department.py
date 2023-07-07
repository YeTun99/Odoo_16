from odoo import fields,api,models

class HrDepartment(models.Model):
    _inherit="hr.department"

    currency_id=fields.Many2one("res.currency")
    limit=fields.Monetary("Expense Price Limit","currency_id",default=100000)

  
    
from odoo import models,fields,api

class ExpenseApprovalLimit(models.Model):
    _name="expense.approval.limit"
    _description="Ap limit"

    name="Approval Limit"
    department_id=fields.Many2one("hr.department",string="Department")
    ap_checker_ids=fields.Many2many("res.users",string="Checker")
    approver_ids = fields.Many2many("res.users", "hr_expense_app_limit_res_user_approver_rel", string="Approver")
    final_approver_ids = fields.Many2many(comodel_name="res.users", relation="hr_expense_res_user_final_approval_rel",
                                          column1= "current_model_aplimit", column2="target_model_res_users", string="Final Apprrover")
    
    currency_id=fields.Many2one('res.currency')
    expense_price_limit=fields.Monetary('currency_id',related='department_id.limit')
    
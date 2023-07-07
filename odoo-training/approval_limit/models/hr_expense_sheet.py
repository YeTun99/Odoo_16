from odoo import models, fields, api
from odoo.exceptions import UserError

class HrDepartment(models.Model):
    _inherit = "hr.expense.sheet"
    approver_check = fields.Boolean(string="Checker", compute="_check_approval", default=False)
    approver = fields.Boolean(string="Approver", compute="_check_approval", default=False)
    final_approver = fields.Boolean(
        string="Final Approver", compute="_check_approval", default=False)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('submit', 'Submitted'),
        ('check', 'Checked'),
        ('approver', 'Approved'),
        ('approve', 'Final Approved'),
        ('post', 'Posted'),
        ('done', 'Done'),
        ('cancel', 'Refused')
    ], string='Status')

    @api.onchange('state')
    def _clear_rule_cache(self):
        self.env['ir.rule'].clear_cache()

    def action_check_sheet(self):
       self.update({
           "state":"check"
       })

    def approve_expense_sheets(self):
        self.update({
            "state":"approve"
        })
    
    
    def action_approve_sheet(self):
        state = 'approver'
        ap_expense_limit = self.get_approver_limit_by_department().mapped("expense_price_limit")
        if self.total_amount < ap_expense_limit[-1]:
            state = 'approve'
        self.update({
                "state":state
            })
    
    def get_approver_limit_by_department(self):
        Aapprover_ids = self.env['expense.approval.limit'].search([
            ('department_id', '=', self.employee_id.department_id.id)
        ],limit=1)
        return Aapprover_ids
    
    @api.depends('state')
    def _check_approval(self):
        for rec in self:
            if rec.state == "submit":
                ap_checker_ids = rec.get_approver_limit_by_department().mapped("ap_checker_ids")
                rec.approver_check = True if self.env.user in ap_checker_ids else False
                rec.approver = False
                rec.final_approver = False
            elif rec.state == "check":
                ap_approver_ids = rec.get_approver_limit_by_department().mapped("approver_ids")
                rec.approver = True if self.env.user in ap_approver_ids else False
                rec.approver_check = False
                rec.final_approver = False
            elif rec.state == "approver":
                ap_expense_limit = rec.get_approver_limit_by_department().mapped("expense_price_limit")
                for i in ap_expense_limit:
                    if rec.total_amount < i:
                        rec.final_approver = True
                    else:
                        ap_final_approver_ids = rec.get_approver_limit_by_department().mapped("final_approver_ids")
                        rec.final_approver = True if self.env.user in ap_final_approver_ids else False
                rec.approver_check = False
                rec.approver = True
            else:
                rec.approver_check = False
                rec.approver = False
                rec.final_approver = False
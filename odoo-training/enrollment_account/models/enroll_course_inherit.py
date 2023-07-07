from odoo import fields,api,models

class EnrollCourseInherit(models.Model):
    _inherit="course_enrollment"

    reference=fields.Many2one('course_enrollment','name')
    def action_do_confirm(self):
        res=super().action_do_confirm()
        journal=self.env["account.journal"].search([("type","=","sale")], limit=1)
        for prop in self:
            self.env["account.move"].create(
                {
                    "partner_id":prop.member_id.partner_id.id,
                    "currency_id":prop.currency_id.id,
                    "enroll_ref":prop.name,
                    "invoice_date":prop.start_date,
                    "move_type":"out_invoice",
                    "journal_id":journal.id,
                    "invoice_line_ids":[
                        (0,0,{
                            "name":prop.name,
                            "quantity":1.0,
                            "price_unit":prop.total_amount,
                        },),(0,0,
                            {
                                "name":"Administrative fees",
                                "quantity":1.0,
                                "price_unit":100.0,
                            },
                        ),
                    ]
                }
            )
        return res
   
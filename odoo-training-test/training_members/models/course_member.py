from odoo import fields,models,api

class Member(models.Model):
    _name="training_members.course_member"
    _description="Training Center Course Member"

    card_number=fields.Char("Card")
    partner_id=fields.Many2one("res.partner",delegate=True,ondelete="cascade",required=True)
     
    @api.model
    def create(self,vals_list):
        vals_list['card_number']=self.env['ir.sequence'].next_by_code('training_members.course_member') or '/'
        return super().create(vals_list)
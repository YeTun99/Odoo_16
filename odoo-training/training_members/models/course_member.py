from odoo import fields,models,api

class Member(models.Model):
    _name="training_members.course_member"
    _description="Training Center Course Member"

    card_number=fields.Char("Card")
    partner_id=fields.Many2one("res.partner",delegate=True,ondelete="cascade",required=True)

from odoo import models,fields

class ResUser(models.Model):
    _inherit="res.users"
    # res,*(res.partner,res.users,etc) config upgrade or command update
    training_center_company=fields.Many2one("res.partner", string="Trainig Center Company") 
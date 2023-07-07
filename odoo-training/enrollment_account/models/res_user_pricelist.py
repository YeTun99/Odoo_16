from odoo import models,fields,api

class ResUser(models.Model):
    _inherit="res.users"
    # res,*(res.partner,res.users,etc) config upgrade or command update
    pricelist=fields.Many2many("product.pricelist") 

   
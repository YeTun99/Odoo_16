from odoo import models,fields,api

class SaleOrderInherit(models.Model):
    _inherit="sale.order"
    # res,*(res.partner,res.users,etc) config upgrade or command update
    payment_method=fields.Selection([
        ('credict','Pay Later'),
        ('cash_down','Pay Now'),
    ],default='credict')
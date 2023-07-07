from odoo import api,fields,models

class ProductTemplate(models.Model):
    _inherit="product.template"

    allow_discount=fields.Boolean("Allow Disccount")
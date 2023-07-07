from odoo import models,fields,api

class CourseParnter(models.Model):
    _inherit="res.partner"
    overdue=fields.Boolean(string="Allow Over Credict")
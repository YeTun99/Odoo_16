from odoo import models,fields,api

class ResUser(models.Model):
    _inherit="res.users"
    warehouse=fields.Many2many("stock.warehouse",string="Default Warehouse")
    @property
    def location_ids(self):
        if self.warehouse:
            return self.env['stock.location'].search([]).filtered(lambda x:x.warehouse_id in self.warehouse)
        else:
            return self.env['stock.location'].search([])
        
    @api.onchange("warehouse")
    def _clear_rule_cache(self):
        self.env['ir.rule'].clear_cache()
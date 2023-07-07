from odoo import models, fields, api


class ScriptRun(models.AbstractModel):
    _name = 'script.run'
    _description = 'Script'

    @api.model
    def run_script(self):
        partner_rec=self.env['res.partner'].sudo().search([('city','!=',False)])
        for partner in partner_rec:
            partner.city=False  
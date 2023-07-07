from odoo import models,fields,api

class InvoiceInherit(models.Model):
    _inherit='account.move'

    enroll_ref=fields.Char("Enrollment Reference")


class InvoiceLineInherit(models.Model):
    _inherit="account.move.line"

    weight=fields.Float("Weight")
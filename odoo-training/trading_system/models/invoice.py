from odoo import fields,api,models
from odoo.exceptions import UserError

class InvoiceUnpaid(models.Model):
    _inherit="account.move"


    @api.onchange("partner_id")
    def partner_onchange(self):
        if self.partner_id and self.move_type=='out_invoice':
            customer_invoice_condition_2=self.env['account.move'].search(
                [('partner_id','=',self.partner_id.id),('payment_state','=','not_paid'),('move_type','=','out_invoice')])
            if customer_invoice_condition_2 :
                raise UserError("You can not select this customer because this customer has unpaid invoice")
            return 
        
            

    @api.onchange("invoice_line_ids")
    def product_qty_onchage(self):
        
        if self.move_type=="out_invoice":
            product_qty=sum(self.invoice_line_ids.filtered_domain([('product_id.detailed_type','!=','service')]).mapped('quantity'))
            service_line=self.invoice_line_ids.filtered_domain([('product_id.detailed_type','=','service')] )    
            service_line.update({
                        'quantity':product_qty})
      
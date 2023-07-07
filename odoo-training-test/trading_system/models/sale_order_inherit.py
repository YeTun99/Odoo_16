from odoo import fields,api,models
from odoo.exceptions import UserError
from datetime import timedelta

class SaleOrderInherit(models.Model):
    _inherit="sale.order"

    # @api.onchange("order_line")
    # def product_qty_onchage(self):
    #     product_quantity=0
    #     for order_line in self.order_line:
            
    #         if order_line.product_template_id.detailed_type != 'service':
    #                 product_quantity+=order_line.product_uom_qty
            
    #         service_line=order_line.order_id.order_line.filtered_domain([('product_template_id.detailed_type','=','service')] )    
           
    #         service_line.update({
    #                     'product_uom_qty':product_quantity})
           


    def action_confirm(self):
        for order in self:
            customer_invoice=self.env['account.move'].search(
                [('partner_id','=',order.partner_id.id),('invoice_date_due','<',fields.datetime.now().date()),('state','=','posted'),
                 ('payment_state','=','not_paid')])
            amount_due =sum(customer_invoice.mapped('amount_residual'))
            customer_invoice_condition2=self.env['account.move'].search(
                [('partner_id','=',order.partner_id.id),('payment_state','=','not_paid')])
            if customer_invoice_condition2 :
                raise UserError(
                    ("You cannot confirm sale order because the customer has unpaid invoice")
                )
            if amount_due > 0 and order.payment_method == 'credict' and not order.partner_id.overdue:
                raise UserError(
                    ("You cannot confirm sale order because the customer has over credict")
                )
        res= super(SaleOrderInherit,self).action_confirm()
        return res
    
    
    # service_product_qty=fields.Float(compute="_compute_service_quantity")

    # @api.depends('order_line.product_uom_qty')
    # def _compute_service_quantity(self):
    #     for product in  self:
    #         product_quantity=0
    #         for line in product.order_line:
    #             if line.product_template_id.detailed_type != 'service':
    #                 product_quantity+=line.product_uom_qty
           
    #         service_line=product.order_line.filtered_domain([('product_template_id.detailed_type','=','service')] )    
    #         return service_line.update({
    #                      'product_uom_qty':product_quantity
    #               })
        
    #         product.service_product_qty=product_quantity

    @api.onchange("partner_id")
    def onchange_partner_id(self):
        if self.partner_id:
            return{
                'domain':
                {
                    'pricelist_id':[('id','in',self.env.user.pricelist.ids)]
                }
            }
    
class SaleOrderLineInherit(models.Model):
    _inherit="sale.order.line"

    weight=fields.Float("Weight")

    def _prepare_invoice_line(self,**optional_values):
        res = super(SaleOrderLineInherit,self)._prepare_invoice_line(**optional_values)
        res['weight']=self.weight
        return res
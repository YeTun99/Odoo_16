from odoo import api, fields, models


class WarehouseReportHelper(models.TransientModel):
    _name = 'stock.report.helper.summary'

    start_date = fields.Datetime()
    end_date = fields.Datetime()
    location_id = fields.Many2one('stock.location')
    product_id = fields.Many2one('product.product')

    def get_moves(self, src_location_ids, dest_location_ids):
        domain = [
            ('product_id', '=', self.product_id.id), 
            ('date', '>', self.start_date), 
            ('date', '<', self.end_date), 
            ('state', '=', 'done')
        ]
        if src_location_ids:
            domain.append(('location_id', 'in', src_location_ids.ids))
        if dest_location_ids:
            domain.append(('location_dest_id', 'in', dest_location_ids.ids))
        return self.env['stock.move'].search(domain)

    def get_total_in(self):
        total = 0
        for loc in self.get_warehouse_locations():
            src = None
            dest = loc
            moves = self.get_moves(src, dest)
            total += sum(moves.mapped('quantity_done'))
        return total

    def get_total_out(self):
        total = 0
        for loc in self.get_warehouse_locations():
            src = loc
            dest = None
            moves = self.get_moves(src, dest)
            total += sum(moves.mapped('quantity_done'))
        return total

    def get_receiving(self):
        total = 0
        for loc in self.get_warehouse_locations():
            src = self.env['stock.location'].search([('usage', '=', 'supplier')])
            dest = loc
            moves = self.get_moves(src, dest)
            total += sum(moves.mapped('quantity_done'))
        return total

    def get_receiving_return(self):
        total = 0
        for loc in self.get_warehouse_locations():
            src = loc
            dest = self.env['stock.location'].search([('usage', '=', 'supplier')])
            moves = self.get_moves(src, dest)
            total += sum(moves.mapped('quantity_done'))
        return total

    def get_transfer_in(self):
        total = 0
        for loc in self.get_warehouse_locations():
            src = self.location_id.id
            dest = loc
            moves = self.get_moves(src, dest)
            total += sum(moves.mapped('quantity_done'))
        return total

    def get_delivery(self):
        total = 0
        for loc in self.get_warehouse_locations():
            src = loc
            dest = self.env['stock.location'].search([('usage', '=', 'customer')])
            moves = self.get_moves(src, dest)
            total += sum(moves.mapped('quantity_done'))
        return total

    def get_delivery_return(self):
        total = 0
        for loc in self.get_warehouse_locations():
            src = self.env['stock.location'].search([('usage', '=', 'customer')])
            dest = loc
            moves = self.get_moves(src, dest)
            total += sum(moves.mapped('quantity_done'))
        return total

    def get_scrap(self):
        total = 0
        for loc in self.get_warehouse_locations():
            src = loc
            for loc2 in self.env['stock.location'].search([('scrap_location', '=', True)]):
                dest = loc2
                moves = self.get_moves(src, dest)
                total += sum(moves.mapped('quantity_done'))
        return total
    
    def get_transfer_out(self):
        total = 0
        for loc in self.get_warehouse_locations():
            src = loc
            dest = self.env['stock.location'].search([('usage', '=', 'transit')])
            moves = self.get_moves(src, dest)
            total += sum(moves.mapped('quantity_done'))
        return total

    def get_adjustment_positive(self):
        total = 0
        for loc in self.get_warehouse_locations():
            src = self.env['stock.location'].search([('name', 'like', 'Inventory adjustment')])
            dest = loc
            moves = self.get_moves(src, dest)
            total += sum(moves.mapped('quantity_done'))
        return total

    def get_adjustment_negative(self):
        total = 0
        for loc in self.get_warehouse_locations():
            src = loc
            dest = self.env['stock.location'].search([('name', 'like', 'Inventory adjustment')])
            moves = self.get_moves(src, dest)
            total += sum(moves.mapped('quantity_done'))
        return total

    def get_warehouse_locations(self):
        # TODO: for now, just use stock location
        #return self.warehouse_id.lot_stock_id
        return self.location_id

    def get_qty(self, to_date):
        total = 0
        for loc in self.get_warehouse_locations():
            total += self.product_id.with_context({'location': loc.id, 'to_date': to_date}).qty_available
            # cache issue with context. without invalidating cache, previous location `qty_available` will be returned instead
            # https://github.com/odoo/odoo/issues/33641
            self.product_id.invalidate_cache(['qty_available'])
        return total

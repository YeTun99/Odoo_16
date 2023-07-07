# -*- coding: utf-8 -*-
# from odoo import http


# class TradingSystem(http.Controller):
#     @http.route('/trading_system/trading_system', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/trading_system/trading_system/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('trading_system.listing', {
#             'root': '/trading_system/trading_system',
#             'objects': http.request.env['trading_system.trading_system'].search([]),
#         })

#     @http.route('/trading_system/trading_system/objects/<model("trading_system.trading_system"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('trading_system.object', {
#             'object': obj
#         })

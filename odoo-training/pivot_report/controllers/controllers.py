# -*- coding: utf-8 -*-
# from odoo import http


# class PivotReport(http.Controller):
#     @http.route('/pivot_report/pivot_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pivot_report/pivot_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pivot_report.listing', {
#             'root': '/pivot_report/pivot_report',
#             'objects': http.request.env['pivot_report.pivot_report'].search([]),
#         })

#     @http.route('/pivot_report/pivot_report/objects/<model("pivot_report.pivot_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pivot_report.object', {
#             'object': obj
#         })

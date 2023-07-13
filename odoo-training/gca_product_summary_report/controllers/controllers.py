# -*- coding: utf-8 -*-
from odoo import http

# class GcaWarehouseTransitionReport(http.Controller):
#     @http.route('/gca_warehouse_transition_report/gca_warehouse_transition_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gca_warehouse_transition_report/gca_warehouse_transition_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gca_warehouse_transition_report.listing', {
#             'root': '/gca_warehouse_transition_report/gca_warehouse_transition_report',
#             'objects': http.request.env['gca_warehouse_transition_report.gca_warehouse_transition_report'].search([]),
#         })

#     @http.route('/gca_warehouse_transition_report/gca_warehouse_transition_report/objects/<model("gca_warehouse_transition_report.gca_warehouse_transition_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gca_warehouse_transition_report.object', {
#             'object': obj
#         })
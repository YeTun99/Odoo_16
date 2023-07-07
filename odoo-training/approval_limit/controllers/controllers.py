# -*- coding: utf-8 -*-
# from odoo import http


# class Approver(http.Controller):
#     @http.route('/approver/approver', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/approver/approver/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('approver.listing', {
#             'root': '/approver/approver',
#             'objects': http.request.env['approver.approver'].search([]),
#         })

#     @http.route('/approver/approver/objects/<model("approver.approver"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('approver.object', {
#             'object': obj
#         })

# -*- coding: utf-8 -*-
# from odoo import http


# class Enrollment(http.Controller):
#     @http.route('/enrollment/enrollment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/enrollment/enrollment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('enrollment.listing', {
#             'root': '/enrollment/enrollment',
#             'objects': http.request.env['enrollment.enrollment'].search([]),
#         })

#     @http.route('/enrollment/enrollment/objects/<model("enrollment.enrollment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('enrollment.object', {
#             'object': obj
#         })

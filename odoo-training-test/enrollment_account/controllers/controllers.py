# -*- coding: utf-8 -*-
# from odoo import http


# class EnrollmentAccount(http.Controller):
#     @http.route('/enrollment_account/enrollment_account', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/enrollment_account/enrollment_account/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('enrollment_account.listing', {
#             'root': '/enrollment_account/enrollment_account',
#             'objects': http.request.env['enrollment_account.enrollment_account'].search([]),
#         })

#     @http.route('/enrollment_account/enrollment_account/objects/<model("enrollment_account.enrollment_account"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('enrollment_account.object', {
#             'object': obj
#         })

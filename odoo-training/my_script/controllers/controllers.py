# -*- coding: utf-8 -*-
# from odoo import http


# class MyScript(http.Controller):
#     @http.route('/my_script/my_script', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_script/my_script/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_script.listing', {
#             'root': '/my_script/my_script',
#             'objects': http.request.env['my_script.my_script'].search([]),
#         })

#     @http.route('/my_script/my_script/objects/<model("my_script.my_script"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_script.object', {
#             'object': obj
#         })

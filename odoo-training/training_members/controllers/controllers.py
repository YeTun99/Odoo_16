# -*- coding: utf-8 -*-
# from odoo import http


# class Odoo-training/trainingMembers(http.Controller):
#     @http.route('/odoo-training/training_members/odoo-training/training_members', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo-training/training_members/odoo-training/training_members/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo-training/training_members.listing', {
#             'root': '/odoo-training/training_members/odoo-training/training_members',
#             'objects': http.request.env['odoo-training/training_members.odoo-training/training_members'].search([]),
#         })

#     @http.route('/odoo-training/training_members/odoo-training/training_members/objects/<model("odoo-training/training_members.odoo-training/training_members"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo-training/training_members.object', {
#             'object': obj
#         })

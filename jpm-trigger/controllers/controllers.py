# -*- coding: utf-8 -*-
# from odoo import http


# class JpmTrigger(http.Controller):
#     @http.route('/jpm_trigger/jpm_trigger/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jpm_trigger/jpm_trigger/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('jpm_trigger.listing', {
#             'root': '/jpm_trigger/jpm_trigger',
#             'objects': http.request.env['jpm_trigger.jpm_trigger'].search([]),
#         })

#     @http.route('/jpm_trigger/jpm_trigger/objects/<model("jpm_trigger.jpm_trigger"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jpm_trigger.object', {
#             'object': obj
#         })

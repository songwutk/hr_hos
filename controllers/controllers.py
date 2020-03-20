# -*- coding: utf-8 -*-
# from odoo import http


# class HrHos(http.Controller):
#     @http.route('/hr_hos/hr_hos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_hos/hr_hos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_hos.listing', {
#             'root': '/hr_hos/hr_hos',
#             'objects': http.request.env['hr_hos.hr_hos'].search([]),
#         })

#     @http.route('/hr_hos/hr_hos/objects/<model("hr_hos.hr_hos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_hos.object', {
#             'object': obj
#         })

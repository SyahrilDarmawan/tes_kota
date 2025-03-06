# -*- coding: utf-8 -*-
# from odoo import http


# class TesKota(http.Controller):
#     @http.route('/tes_kota/tes_kota', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tes_kota/tes_kota/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('tes_kota.listing', {
#             'root': '/tes_kota/tes_kota',
#             'objects': http.request.env['tes_kota.tes_kota'].search([]),
#         })

#     @http.route('/tes_kota/tes_kota/objects/<model("tes_kota.tes_kota"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tes_kota.object', {
#             'object': obj
#         })

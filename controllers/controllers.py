# -*- coding: utf-8 -*-
# from odoo import http


# class GoogleSpreadsheetPurchase(http.Controller):
#     @http.route('/google_spreadsheet_purchase/google_spreadsheet_purchase', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/google_spreadsheet_purchase/google_spreadsheet_purchase/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('google_spreadsheet_purchase.listing', {
#             'root': '/google_spreadsheet_purchase/google_spreadsheet_purchase',
#             'objects': http.request.env['google_spreadsheet_purchase.google_spreadsheet_purchase'].search([]),
#         })

#     @http.route('/google_spreadsheet_purchase/google_spreadsheet_purchase/objects/<model("google_spreadsheet_purchase.google_spreadsheet_purchase"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('google_spreadsheet_purchase.object', {
#             'object': obj
#         })

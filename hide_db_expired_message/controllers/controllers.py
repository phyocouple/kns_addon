# -*- coding: utf-8 -*-
# from odoo import http


# class HideDbExpiredMessage(http.Controller):
#     @http.route('/hide_db_expired_message/hide_db_expired_message', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hide_db_expired_message/hide_db_expired_message/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hide_db_expired_message.listing', {
#             'root': '/hide_db_expired_message/hide_db_expired_message',
#             'objects': http.request.env['hide_db_expired_message.hide_db_expired_message'].search([]),
#         })

#     @http.route('/hide_db_expired_message/hide_db_expired_message/objects/<model("hide_db_expired_message.hide_db_expired_message"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hide_db_expired_message.object', {
#             'object': obj
#         })

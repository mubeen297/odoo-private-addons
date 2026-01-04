import logging
import werkzeug
import base64
import itertools
import json
from datetime import date, datetime, timedelta
from odoo.http import request
from odoo import api, http, SUPERUSER_ID
from odoo.service import security


# class CashierLessCheckoutController(http.Controller):
#
#     @http.route(['/start_order'], type='http', auth="user", website=True, csrf=False)
#     def start_order(self, **kw):
#         return http.request.render('cashierless_checkout.start_order', {})
#
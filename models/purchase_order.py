import base64
import json
import io
import os
from .spreadsheet_connector import GoogleSpreadsheet

from odoo import fields, models


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def send_order_to_spreadsheet(self):
        for rec in self:
            credentials = self.env.ref('google_spreadsheet_purchase.spreadsheet_panel_settings')
            connect = GoogleSpreadsheet().connect(credentials)

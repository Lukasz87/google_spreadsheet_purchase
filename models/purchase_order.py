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
            val = self.env['res.config.settings']
            # TODO - move to config in odoo
            # spreadsheet_credentials = base64.b64decode(rec.partner_id.spreadsheet_credentials).decode('utf-8')
            # credentials_file = json.loads(spreadsheet_credentials)
            credentials_file = f'{os.path.dirname(os.path.realpath(__file__))}/credentials' # TODO - temp connection
            connect = GoogleSpreadsheet().connect(credentials_file)

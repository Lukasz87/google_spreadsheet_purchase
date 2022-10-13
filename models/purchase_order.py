from .spreadsheet_connector import GoogleSpreadsheet
import pandas as pd

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def send_order_to_spreadsheet(self):
        for rec in self:
            credentials = self.env.ref('google_spreadsheet_purchase.spreadsheet_panel_settings')
            vendor = rec.partner_id
            connect = GoogleSpreadsheet(credentials.spreadsheet_credentials)
            vendor = self.env['spreadsheet.panel'].search([('vendor_id', '=', vendor.id)])
            if len(vendor) > 1:
                raise UserError(_('More then one vendor configuration!'))
            spreadsheet = connect.get_spreadsheet(vendor.spreadsheet_id)
            df = pd.DataFrame(spreadsheet.sheet1.get_all_records()) # TODO - add choose sheet
            print(df)

from odoo import fields, models


class ResConfigSettingsSpreadsheetPanel(models.TransientModel):
    _inherit = 'res.config.settings'

    spreadsheet_credentials = fields.Binary('Spreadsheet Credentials')

from odoo import fields, models


class ResConfigSettingsSpreadsheetPanel(models.Model):
    _name = 'res.config.spreadsheet.panel'

    spreadsheet_credentials = fields.Binary('Spreadsheet Credentials')

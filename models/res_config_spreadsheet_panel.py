from odoo import fields, models


class ResConfigSettingsSpreadsheetPanel(models.Model):
    _name = 'res.config.spreadsheet.panel'

    spreadsheet_credentials = fields.Text('Spreadsheet Credentials json')
    scopes = fields.Text('Spreadsheet Scopes')
    service_account = fields.Char('Spreadsheet Scopes')
    columns = fields.One2many('res.config.spreadsheet.panel.columns', 'spreadsheet_panel')

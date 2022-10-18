from odoo import fields, models


class ResConfigSettingsSpreadsheetPanel(models.Model):
    _name = 'res.config.spreadsheet.panel.columns'

    column_name = fields.Char('Spreadsheet Column Name')
    required = fields.Boolean('Column Required')
    spreadsheet_panel = fields.Many2one('res.config.spreadsheet.panel')

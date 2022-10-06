from odoo import fields, models


class SpreadsheetPanel(models.Model):
    _name = 'spreadsheet.panel'
    _description = "Spreadsheet Panel"

    spreadsheet_credentials = fields.Binary('Spreadsheet Credentials')  # TODO Temp -remove



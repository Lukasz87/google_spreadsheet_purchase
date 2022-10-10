from odoo import fields, models


class SpreadsheetPanel(models.Model):
    _name = 'spreadsheet.panel'
    _description = "Spreadsheet Panel"

    vendor = fields.Many2one('res.partner', required=True)
    spreadsheet_id = fields.Char('Spreadsheet ID')




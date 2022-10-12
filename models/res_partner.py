from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    spreadsheet_integration = fields.Boolean('Spreadsheet integration')
    spreadsheet_id = fields.Char('Google Spreadsheet ID')

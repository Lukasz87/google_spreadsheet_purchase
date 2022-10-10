from odoo import fields, models


class Partner(models.Model):
    _inherit = ['res.partner']

    spreadsheet_integration = fields.Boolean('Spreadsheet integration')

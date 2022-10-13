from odoo import fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    spreadsheet_integration_panel = fields.One2many('spreadsheet.panel', 'vendor_id')


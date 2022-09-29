from odoo import fields, models
from odoo.exceptions import AccessError


class Partner(models.Model):
    _inherit = ['res.partner']

    spreadsheet_integration = fields.Boolean('Spreadsheet integration')

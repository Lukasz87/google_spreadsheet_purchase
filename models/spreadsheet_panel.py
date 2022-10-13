from odoo import fields, models, api


class SpreadsheetPanel(models.Model):
    _name = 'spreadsheet.panel'
    _description = "Spreadsheet Panel"

    vendor_id = fields.Many2one('res.partner', required=True)
    spreadsheet_integration = fields.Boolean()
    spreadsheet_id = fields.Char()

    _sql_constraints = [
        ('vendor_unique', 'unique (vendor_id)', 'Vendor need to be unique!'),
    ]

    # @api.onchange("vendor")
    # def _onchange_spreadsheet_id(self):
    #     ...






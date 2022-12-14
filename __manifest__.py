# -*- coding: utf-8 -*-
{
    'name': "google_spreadsheet_purchase",

    'summary': """
        Odoo Purchase Order in google spreadsheet for vendors
        """,

    'description': """
        Module add functionality to send PO to google spreadsheet.
        Each Vendor have own spreadsheet when he can change PO status.
        Vendor can also add comments in Google spreadsheet to order and it will update 
        PO/Picking documents.
    """,

    'author': "Lukasz87",
    'website': "https://github.com/Lukasz87/google_spreadsheet_purchase",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Purchase Management',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/purchase_order_views.xml',
        'views/spreadsheet_panel.xml',
        'views/res_config_settings_views.xml',
        'views/res_partner_views.xml',
        'data/res_config_spreadsheet_panel.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

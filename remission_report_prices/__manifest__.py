# Copyright 2020 TECNOSOFTWARE S.A.S (<http://www.tecnosoftware.co>)
# -*- coding: utf-8 -*-
{
    'name': "Stock remission report",
    'summary': """
        Module for printing referrals with product data including the
        sale price, discount for the price list applied to the contact and the
        minimum value to sell""",
    'author': "Jose Gonzalez / Tecnosoftware S.A.S",
    'website': "https://www.tecnosoftware.co",
    "maintainers": ["tecnosoftcol"],
    'category': "Warehouse",
    "license": "OPL-1",
    'version': "14.0.1.0.0",
    "application": False,
    "installable": True,
    'depends': ['sale', 'stock'],
    'data': [
        'views/report_view.xml',
        'views/remission_report_view.xml',
        'security/remission_report_prices_security.xml',
        'security/ir.model.access.csv'
    ],
}

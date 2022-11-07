# Copyright 2020 TECNOSOFTWARE S.A.S (<http://www.tecnosoftware.co>)
# -*- coding: utf-8 -*-
{
    "name": "Stock remission report",
    "summary": """ Module for printing referrals with product data including the
        sale price, discount for the price list applied to the contact and the
        minimum value to sell""",
    "version": "15.0.1.0.0",
    "author": "Jose Gonzalez / Tecnosoftware S.A.S",
    "website": "https://www.tecnosoftware.co",
    "maintainers": ["tecnosoftcol"],
    "license": "OPL-1",
    "application": False,
    "installable": True,
    "depends": ["base", "sale", "stock"],
    "data": [
        'views/report_view.xml',
        'views/remission_report_view.xml',
        'security/remission_report_prices_security.xml',
        'security/ir.model.access.csv'
    ],
}

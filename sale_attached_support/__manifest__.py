# Copyright 2020 TECNOSOFTWARE S.A.S (<http://www.tecnosoftware.co>)
# -*- coding: utf-8 -*-
{
    "name": "Sale Attached Support",
    "summary": """Validates if a sale order has a backup
    document to create""",
    "version": "14.0.1.0.0",
    'author': "Jose Gonzalez / Tecnosoftware S.A.S",
    'website': "https://www.tecnosoftware.co",
    "maintainers": ["tecnosoftcol"],
    "license": "OPL-1",
    'version': "14.0.1.0.0",
    "application": False,
    "installable": True,
    "depends": ["base", "sale"],
    "data": [
        "views/sale_order_views.xml",
    ],
}

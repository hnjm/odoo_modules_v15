# Copyright 2020 TECNOSOFTWARE S.A.S (<http://www.tecnosoftware.co>)
# -*- coding: utf-8 -*-
{
    "name": "Purchase Attached Support",
    "summary": """Validates if a quotation has a support
    document to convert it to purchase order""",
    "version": "15.0.1.0.0",
    "author": "Jose Gonzalez / Tecnosoftware S.A.S",
    "website": "https://www.tecnosoftware.co",
    "maintainers": ["tecnosoftcol"],
    "license": "OPL-1",
    "application": False,
    "installable": True,
    "depends": ["base", "purchase"],
    "data": [
        "views/purchase_order_views.xml",
    ],
}

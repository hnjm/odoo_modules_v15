# Copyright 2020 TECNOSOFTWARE S.A.S (<http://www.tecnosoftware.co>)
# -*- coding: utf-8 -*-
{
    "name": "Document Partner Sale",
    "summary": """Add identification number(vat) and street of partner in tree view of sale order""",
    "version": "15.0.1.0.0",
    "author": "Jose Gonzalez / Tecnosoftware S.A.S",
    "website": "https://www.tecnosoftware.co",
    "maintainers": ["tecnosoftcol"],
    "license": "OPL-1",
    "application": False,
    "installable": True,
    "depends": ["base", "base_vat", "sale"],
    "data": [
        'views/document_partner_view.xml'
    ],
}

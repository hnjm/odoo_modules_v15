# Copyright 2020 TECNOSOFTWARE S.A.S (<http://www.tecnosoftware.co>)
# -*- coding: utf-8 -*-
{
    "name": "Filing Supplier Invoices",
    "summary": """Add a invoice support to invoices & clasificate a purchase orders by the status of settling 
    """,
    "version": "15.0.1.0.0",
    "author": "Jose Gonzalez / Tecnosoftware S.A.S",
    "website": "https://www.tecnosoftware.co",
    "maintainers": ["tecnosoftcol"],
    "license": "OPL-1",
    "application": False,
    "installable": True,
    "depends": ['base', 'purchase', 'account'],
    "data": [
        'security/filing_supplier_invoices_security.xml',
        'security/ir.model.access.csv',
        'views/purchase_order_views.xml',
        'views/account_move_views.xml',
        'views/document_views.xml',
        'views/documents_menuitems.xml',
        'data/ir_sequence_data.xml',
    ],
    "demo": [
        'demo/documents_demo.xml'
    ]

}

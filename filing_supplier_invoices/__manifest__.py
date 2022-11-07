# -*- coding: utf-8 -*-
{
    'name': "Filing Supplier Invoices",
    'summary': """
       """,
    'author': "Jose Gonzalez / Tecnosoftware S.A.S",
    'website': "https://www.tecnosoftware.co",
    "maintainers": ["tecnosoftcol"],
    'category': "Warehouse",
    "license": "OPL-1",
    'version': "14.0.1.0.0",
    "application": False,
    "installable": True,
    'depends': ['purchase', 'account'],
    'data': [
        'security/filing_supplier_invoices_security.xml',
        'security/ir.model.access.csv',
        'views/purchase_order_views.xml',
        'views/account_move_views.xml',
        'views/document_views.xml',
        'views/documents_menuitems.xml',
        'data/ir_sequence_data.xml',
    ],
    'demo': [
        'demo/documents_demo.xml'
    ]

}

# Copyright 2020 TECNOSOFTWARE S.A.S (<http://www.tecnosoftware.co>)
# -*- coding: utf-8 -*-
{
    "name": "Res Partner References",
    "summary": """Add a partner references address, this references is used in sale orders created
    """,
    "version": "15.0.1.0.0",
    "author": "Jose Gonzalez / Tecnosoftware S.A.S",
    "website": "https://www.tecnosoftware.co",
    "maintainers": ["tecnosoftcol"],
    "license": "OPL-1",
    "application": False,
    "installable": True,
    "depends": ["base", "sale", "account", "l10n_co_extra", "neighborhood_partner_address"],
    "data": [
        "security/ir.model.access.csv",
        "security/sale_security.xml",
        "views/res_partner_reference_views.xml",
        "views/sale_order_views.xml",
        "views/account_move_views.xml",
        "views/res_config_settings_views.xml",
        "report/sale_report_templates.xml",
        "report/report_invoice.xml"
    ],
}

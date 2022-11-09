# -*- coding: utf-8 -*-
# Copyright 2020 Alcides Vega (<http://www.tecnosoftware.co>)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Agrega el Barrio y su codigo postal asociado en contactos',
    'summary': """Agrega los campos los campos de barrio el codigo postal asociado en la informacion del contacto """,
    'version': '15.0.1.0.0',
    'category': 'Extra Tools',
    'author': 'Alcides Vega [TECNOSOFTWARE S.A.S.]',
    'website': 'http://www.tecnosoftware.co',
    'license': 'AGPL-3',
    'depends': ['contacts', 'partner_delivery_zone', 'cup_is_customer_is_vendor', 'l10n_co_extra'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_barrio.xml',
        'views/res_city_barrios_view.xml',
    ],
    'post_init_hook': 'post_init_hook',
    'uninstall_hook': 'uninstall_hook',
}

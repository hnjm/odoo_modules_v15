# Copyright 2022 Alcides Vega (<http://www.tecnosoftware.co>)
# -*- coding: utf-8 -*-
{
    'name': "Colombia: Campos Extra Localización",

    'summary': """
        Unificación de campos necesarios para la localización colombiana""",
    'description': """
        Campos Extra Colombia
        
        - Ciudades y códigos postales según listado DIAN v1.8
        - Nombre de contacto separado para personas naturales
        - Tipo de documento con código y dígito verificador 
        - Clasificador CIIU
        - UNSPSC ‐ Código Estándar de Productos y Servicios de Naciones Unidas, V.14.080, Producto -> Clase -> Familia -> Segmento 
        - Código de Identificación en las unidades de medida
        - Listado de Bancos Colombianos
    """,
    'author': 'José Luis Vizcaya López',
    'company': 'José Luis Vizcaya López',
    'maintainer': 'José Luis Vizcaya López',
    'website': 'https://github.com/birkot',
    'category': 'Localization',
    'version': '15.0.1.0.0',
    'depends': ['base', 'base_vat', 'base_address_city', 'contacts', 'l10n_latam_base', 'product', 'uom', 'l10n_co_edi_jorels'],
    "post_init_hook": "post_init_hook",
    "external_dependencies": {"python": ["pandas"]},
    'data': [
        'views/res_city_view.xml',
        'views/res_city_zip_view.xml',
        'views/res_company_view.xml',
        'views/res_country_state_views.xml',
        'views/res_country_view.xml',
        'views/res_partner_view.xml',
        'views/res_bank_view.xml',
        'views/product_template_views.xml',
        'views/product_uom_views.xml',
        'data/res.country.state.csv',
        'data/res.city.csv',
        'data/ciiu.csv',
        'data/res.bank.csv',
        'data/product.uom.code.csv',
        'data/product_scheme_data.xml',
        'security/ir.model.access.csv',
    ],
    'images': [
        'static/description/thumbnail.png',
    ],
    'license': 'Other proprietary',
    "price": 50,
    "currency": "USD",
}

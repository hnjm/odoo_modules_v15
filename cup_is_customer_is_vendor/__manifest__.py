{
    "name": "Is a Customer and Is a Vendor",
    "summary": """Add Field Is a Customer And Is a Vendor""",
    "license": "LGPL-3",
    "images": ["static/description/cupdev2.png"],
    "author": "Yusup Nur Karimah",
    "category": "Extra Tools",
    "version": "14.0.1.0.1",
    # any module necessary for this one to work correctly
    "depends": ["base", "account", "sale_management", "purchase"],
    # always loaded
    "data": [
        # 'security/ir.model.access.csv',
        "views/views.xml",
    ],
}

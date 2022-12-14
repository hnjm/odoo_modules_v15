{
    'name': "Dynamic Progress Bar",

    'summary': """
        Progress bar for operations that take more than 5 seconds.
    """,

    # 'description': """
    # Adds dynamic progress bar and cancel button to gray waiting screen.
    # Try to import some CSV file to any model to see it in action.
    # """,

    'author': "Grzegorz Marczyński",
    'category': 'Productivity',
    'website': 'https://github.com/gmarczynski/odoo-web-progress',

    "version": "15.0.1.0.0",

    'depends': ['web',
                'bus',
                'base_import',
                ],

    'data': [
        'security/ir.model.access.csv',
    ],

    'demo': [
    ],
    'images': ['static/description/progress_bar_loading_compact.gif',
               'static/description/progress_bar_loading_cancelling.gif',
               'static/description/progress_bar_loading_systray.gif',
               ],
    'assets': {
        'web.assets_backend': [
            'web_progress/static/src/js/loading.js',
            'web_progress/static/src/js/progress_bar.js',
            'web_progress/static/src/js/ajax.js',
            'web_progress/static/src/js/progress_menu.js',
            'web_progress/static/src/css/views.css'
        ],
        'web.assets_qweb': [
            'web_progress/static/src/xml/progress_bar.xml',
            'web_progress/static/src/xml/web_progress_menu.xml'
        ],
    },

    'license': 'LGPL-3',

    'installable': True,
    'auto_install': True,
    'application': False,
}

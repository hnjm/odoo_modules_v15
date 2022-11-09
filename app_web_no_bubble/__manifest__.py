# Copyright 2016 Savoir-faire Linux
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
# "Savoir-faire Linux, " "Odoo Community Association (OCA)",

{
    "name": "Web No Bubble",
    "version": "15.0.1.0.0",
    'author': 'Sunpop.cn',
    "website": "https://github.com/OCA/web",
    "license": "AGPL-3",
    "category": "Web",
    "summary": "Remove the bubbles from the web interface",
    "depends": ["web"],
    # "data": ["views/web_no_bubble.xml"],
    "installable": True,
    "application": False,
    'assets': {
        'web.assets_backend': [
            'app_web_no_bubble/static/src/css/web_no_bubble.scss',
        ],
    },
}

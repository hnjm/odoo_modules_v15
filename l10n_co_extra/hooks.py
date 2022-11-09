
from odoo import SUPERUSER_ID, api


def post_init_hook(cr, _):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        env["res.city.zip"]._load_zips_dian()
        env["unspsc.product"]._load_unspsc_product()

# © 2014-2016 Camptocamp SA
# @author: Nicolas Bessi
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResCountry(models.Model):
    """Override default adresses formatting of countries"""
    _inherit = 'res.country'

    address_format = fields.Text(
        default=(
            "%(street)s %(barrio)s\n%(street2)s\n"
            "%(city)s %(zip)s\n"
            "%(state_code)s %(country_name)s"
        )
    )

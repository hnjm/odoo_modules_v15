# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    group_reference_address = fields.Boolean(
        "References Addresses", implied_group='res_partner_reference.group_references_address')

# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class Partner(models.Model):
    _inherit = 'res.partner'

    child_reference_ids = fields.One2many(
        'res.partner.reference', 'parent_id', string='Addresses', domain=[('active', '=', True)])

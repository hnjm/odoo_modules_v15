# -*- coding: utf-8 -*-

from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = 'account.move'

    partner_delivery_reference = fields.Many2one(comodel_name='res.partner.reference', string='Delivery Address', required=False,
                                                 store=True, domain="[('parent_id', '=',partner_id),('type_reference', '=', 'delivery')]")

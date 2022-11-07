# -*- coding: utf-8 -*-

from odoo import _, api, fields, models


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    partner_invoice_reference = fields.Many2one('res.partner.reference', string='Invoice Address',
                                                domain="[('parent_id', '=',partner_id),('type_reference', '=', 'invoice')]")

    partner_delivery_reference = fields.Many2one('res.partner.reference', string='Delivery Address',
                                                 domain="[('parent_id', '=',partner_id),('type_reference', '=', 'delivery')]")

    def _clear_partner_invoice_reference(self):
        self.partner_invoice_reference = None

    def _clear_partner_delivery_reference(self):
        self.partner_delivery_reference = None

    @api.onchange("partner_id")
    def onchange_partner_references_module(self):
        self._clear_partner_invoice_reference()
        self._clear_partner_delivery_reference()

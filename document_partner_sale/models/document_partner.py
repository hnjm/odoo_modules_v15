# -*- coding: utf-8 -*-

from odoo import models, fields


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    vat_to_show = fields.Char(
        string="VAT", related='partner_id.vat', store=True)

    street_to_show = fields.Char(
        string="Street", related='partner_id.street', store=True)

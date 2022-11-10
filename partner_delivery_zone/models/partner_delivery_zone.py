# Copyright 2018 Tecnativa - Sergio Teruel
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from odoo import fields, models


class PartnerDeliveryZone(models.Model):
    _name = "partner.delivery.zone"
    _description = "Partner delivery zone"

    city_id = fields.Many2one(
        'res.city', string='Ciudad', ondelete='restrict', required=False)
    code = fields.Char()
    name = fields.Char(string="Zone", required=True)
    active = fields.Boolean(default=True)

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields

class ResPartner(models.Model):
    _inherit = 'res.partner'

    localidad_id = fields.Many2one('res.city.barrios', string='Barrio')
    barrio = fields.Char('Barrio')

    @api.model
    def _address_fields(self):
        fields = super(ResPartner, self)._address_fields()
        fields.append('barrio')
        return fields

    def _display_address(self, without_company=False):
        """Remove empty lines which can happen when barrio field is empty."""
        res = super(ResPartner, self)._display_address(
            without_company=without_company)
        while '\n\n' in res:
            res = res.replace('\n\n', '\n')
        return res

    @api.onchange('localidad_id')
    def _onchange_localidad_id(self):
        if self.localidad_id:
            self.barrio = self.localidad_id.name
            self.delivery_zone_id = self.localidad_id.zona_id
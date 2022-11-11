# -*- coding: utf-8 -*-


from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    @api.depends('zip', 'country_id')
    def _compute_postal_id(self):
        for rec in self:
            if rec.zip and rec.country_id and rec.country_id.code == 'CO':
                postal_obj = rec.env['l10n_co_edi_jorels.postal']
                postal_search = postal_obj.sudo().search(
                    [('name', '=', rec.zip.zfill(6))])
                if postal_search:
                    rec.postal_id = postal_search[0].id
                    rec.postal_department_id = rec.env['l10n_co_edi_jorels.departments'].sudo().search(
                        [('code', '=', rec.postal_id.department_id.code)]
                    )[0].id
                    rec.postal_municipality_id = rec.env['l10n_co_edi_jorels.municipalities'].sudo().search(
                        [('code', '=', rec.postal_id.municipality_id.code)]
                    )[0].id
            else:
                rec.postal_id = None
                rec.postal_department_id = None
                rec.postal_municipality_id = None

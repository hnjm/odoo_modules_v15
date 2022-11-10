# coding: utf-8

from odoo import fields, models, api


class City(models.Model):
    _inherit = 'res.city'

    codigo_municipio = fields.Char("Código municipio")

    zip_ids = fields.One2many(
        "res.city.zip", "city_id", string="Códigos postales")

    zipcode = fields.Char(string='C.P.', compute='_zipcode')

    @api.depends('codigo_municipio')
    def _zipcode(self):
        for rec in self:
            if rec.codigo_municipio:
                rec.zipcode = str(rec.codigo_municipio).zfill(5)
            else:
                rec.zipcode = ''

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        if not args:
            args = []

        if name:
            state = self.search([
                '|',
                ('name', operator, name),
                ('codigo_municipio', operator, name)] + args, limit=limit)
        else:
            state = self.search([], limit=100)

        return state.name_get()

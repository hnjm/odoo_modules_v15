# Copyright 2020 Alcides Vega <proyectos@tecnosoftware.co>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ResCityBarrios(models.Model):

    _name = "res.city.barrios"
    _order = "name asc"

    name = fields.Char('Nombre', required=True)
    city_id = fields.Many2one(
        'res.city',
        'Ciudad/Municipio',
        required=True,
    )
    zona_id = fields.Many2one(
        'partner.delivery.zone',
        'Zona de entrega',
        required=True,
    )
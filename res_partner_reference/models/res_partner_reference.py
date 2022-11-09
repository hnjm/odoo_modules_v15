# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ResPartnerReference(models.Model):

    _name = "res.partner.reference"

    _description = "Address asociated to partner"

    _rec_name = "reference_name"

    parent_id = fields.Many2one(
        'res.partner', string='Related Partner', index=True)

    reference_name = fields.Char(string="Name", required=True)

    type_reference = fields.Selection(
        [
            ('contact', 'Contact'),
            ('invoice', 'Invoice Address'),
            ('delivery', 'Delivery Address'),
        ], string='Reference Type',
        default='invoice',
        help="Invoice & Delivery addresses are used in sales orders.")

    # address fields
    street = fields.Char()
    zip_id = fields.Many2one("res.city.zip", "Código postal")
    zip = fields.Char(change_default=True)
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State',
                               ondelete='restrict')

    country_id = fields.Many2one(
        'res.country', string='Country', ondelete='restrict')
    email = fields.Char()

    phone = fields.Char()
    mobile = fields.Char()

    comment = fields.Text(string='Notes')

    active = fields.Boolean(default=True)

    color = fields.Integer(string='Color Index', default=0)

    country_enforce_cities = fields.Boolean(
        related='country_id.enforce_cities', readonly=True)

    city_id = fields.Many2one('res.city', string='City of Address')

    function = fields.Char(string='Job Position')

    title = fields.Many2one('res.partner.title')

    localidad_id = fields.Many2one('res.city.barrios', string='Barrio')
    barrio = fields.Char('Barrio')

    @api.onchange('localidad_id')
    def _onchange_localidad_id(self):
        if self.localidad_id:
            self.barrio = self.localidad_id.name

    @api.onchange("city_id")
    def _onchange_city_id(self):
        if self.zip_id and self.city_id != self.zip_id.city_id:
            self.update({"zip_id": False, "zip": False, "city": False})
        if self.city_id and self.country_enforce_cities:
            zip_principal = False
            if len(self.city_id.zip_ids) > 0:
                zip_principal = self.city_id.zip_ids[0].name
                self.update(
                    {"zip": zip_principal, "zip_id": self.city_id.zip_ids[0].id})
            return {"domain": {"zip_id": [("city_id", "=", self.city_id.id)]}}
        return {"domain": {"zip_id": []}}

    @api.onchange("zip_id")
    def _onchange_zip_id(self):
        if self.zip_id:
            vals = {
                "city_id": self.zip_id.city_id,
                "zip": self.zip_id.name,
                "city": self.zip_id.city_id.name,
            }
            if self.zip_id.city_id.country_id:
                vals.update({"country_id": self.zip_id.city_id.country_id})
            if self.zip_id.city_id.state_id:
                vals.update({"state_id": self.zip_id.city_id.state_id})
            self.update(vals)
        elif not self.country_enforce_cities:
            self.city_id = False

    @api.constrains("zip_id", "country_id", "city_id", "state_id")
    def _check_zip(self):
        if self.env.context.get("skip_check_zip"):
            return
        for rec in self:
            if not rec.zip_id:
                continue
            if rec.state_id and rec.zip_id.city_id.state_id != rec.state_id:
                raise ValidationError(
                    _("The state of the partner %s differs from that in " "location %s")
                    % (rec.name, rec.zip_id.name)
                )
            if rec.country_id and rec.zip_id.city_id.country_id != rec.country_id:
                raise ValidationError(
                    _(
                        "The country of the partner %s differs from that in "
                        "location %s"
                    )
                    % (rec.name, rec.zip_id.name)
                )
            if rec.city_id and rec.type_reference != 'contact' and rec.zip_id.city_id != rec.city_id:
                raise ValidationError(
                    _("The city of partner %s differs from that in " "location %s")
                    % (rec.name, rec.zip_id.name)
                )

    @api.onchange("state_id")
    def _onchange_state_id(self):
        vals = {}
        if self.state_id.country_id:
            vals.update({"country_id": self.state_id.country_id})
        if self.zip_id and self.state_id != self.zip_id.city_id.state_id:
            vals.update({"zip_id": False, "zip": False, "city": False})
        self.update(vals)
        if self.state_id and not self.zip_id:
            cities_ids = self.env['res.city'].search(
                [('state_id', '=', self.state_id.id)]).ids
            return {'domain': {'zip_id': [('city_id', 'in', cities_ids)],
                               'city_id': [('id', 'in', cities_ids)]}}

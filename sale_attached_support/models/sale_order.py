# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    definitive_attachments = fields.Many2many(
        comodel_name="ir.attachment",
        string="Sale Order Support (PDF-JPG)",
    )

    @api.constrains('definitive_attachments')
    def _check_file(self):
        FILES_ALLOWED = ['pdf', 'jpg', 'jpeg', 'png', 'bmp']
        for file in self.definitive_attachments:
            if str(file.mimetype.split("/")[-1]) not in FILES_ALLOWED:
                raise ValidationError(
                    _("Cannot upload file different from PDF or IMAGE file"))

    def action_confirm(self):
        for record in self:
            definitive = record.definitive_attachments

            if definitive:
                res = super(SaleOrder, record).action_confirm()
            else:
                raise ValidationError(
                    _(
                        "The sale order does not have the necessary supporting "
                        "document to be confirmed"
                    )
                )

        return res

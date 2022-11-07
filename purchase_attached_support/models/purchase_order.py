# -*- coding: utf-8 -*-

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    definitive_attachments = fields.Many2many(
        comodel_name="ir.attachment",
        string="Purchase Support (PDF-JPG)",
    )

    @api.constrains('definitive_attachments')
    def _check_file(self):
        FILES_ALLOWED = ['pdf', 'jpg', 'jpeg', 'png', 'bmp']
        for file in self.definitive_attachments:
            if str(file.mimetype.split("/")[-1]) not in FILES_ALLOWED:
                raise ValidationError(
                    _("Cannot upload file different from PDF or IMAGE file")
                )

    def button_confirm(self):
        for record in self:
            definitive = record.definitive_attachments

            if definitive:
                res = super(PurchaseOrder, record).button_confirm()
            else:
                raise ValidationError(
                    _(
                        "The quotation does not have the necessary supporting "
                        "document to be confirmed"
                    )
                )

        return res

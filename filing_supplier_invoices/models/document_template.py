# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Document(models.Model):

    _name = 'document.template'

    _description = 'Document Template'

    document_type_id = fields.Many2one(
        'document.type', string='Document Type', required=True)

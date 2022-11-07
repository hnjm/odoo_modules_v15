# -*- coding: utf-8 -*-

from odoo import api, fields, models


class DocumentType(models.Model):

    _name = 'document.type'

    _description = 'Type of Document'

    name = fields.Char(string='Name', required=True)

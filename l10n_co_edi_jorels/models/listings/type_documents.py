# -*- coding: utf-8 -*-
#
#   l10n_co_edi_jorels
#   Copyright (C) 2022  Jorels SAS
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU Affero General Public License as published
#   by the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU Affero General Public License for more details.
#
#   You should have received a copy of the GNU Affero General Public License
#   along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#   email: info@jorels.com
#

import logging

from odoo import fields, models

_logger = logging.getLogger(__name__)


class TypeDocuments(models.Model):
    _name = "l10n_co_edi_jorels.type_documents"
    _inherit = "l10n_co_edi_jorels.languages"
    _description = "Document types"

    cufe_algorithm = fields.Char(string="CUFE algorithm", required=False, readonly=True)
    prefix = fields.Char(string="Prefix", required=False, readonly=True)
    type = fields.Char(string="Document type", required=False, readonly=True)

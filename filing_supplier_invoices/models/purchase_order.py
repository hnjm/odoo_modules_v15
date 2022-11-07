from odoo import api, fields, models, _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    status_settling = fields.Selection(string='Status of Settling',
                                       selection=[
                                           ('without_filing', 'Without Filing'),
                                           ('partially_settled',
                                               'Partially Settled'),
                                           ('settled', 'Settled')
                                       ], required=True, default='without_filing')

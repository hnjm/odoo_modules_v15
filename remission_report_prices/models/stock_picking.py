from odoo import api, fields, models, _


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # PDF Report
    def print_remission_report(self):
        return self.env.ref('remission_report_prices.action_report_remission').report_action(self)

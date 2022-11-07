from odoo import api, fields, models, _


class AccountMove(models.Model):
    _inherit = 'account.move'

    filing_number = fields.Many2one(
        comodel_name='document.document', required=True, string='Filing Number', store=True, domain="[('partner_id', '=',partner_id),('state', '=', 'confirmed')]")

    filing_status_number_to_show = fields.Char(
        string="Filing Number", related='filing_number.name', store=True)

    @api.onchange("filing_number")
    def onchange_filing_number(self):
        self.invoice_date = self.filing_number.filing_date
        self.ref = self.filing_number.document_number

    def action_post(self):
        self.filing_number.update_state_invoiced()
        return super().action_post()

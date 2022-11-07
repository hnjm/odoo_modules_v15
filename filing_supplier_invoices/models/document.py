# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Document(models.Model):

    _inherit = 'document.template'

    _name = 'document.document'

    _description = 'Document'

    _rec_name = "name_to_show"

    name = fields.Char(string='Document Filed Reference', required=True, copy=False, readonly=True, states={
                       'draft': [('readonly', False)]}, index=True, default=lambda self: _('New'))

    filing_date = fields.Date(
        string='Date Filing', required=True, default=fields.Datetime.now)

    partner_id = fields.Many2one(
        'res.partner', string='Vendor', required=True)

    document_number = fields.Char(
        string='Supplier invoice number', required=True)

    document_date = fields.Date(
        string='Supplier invoice date', required=True,)

    document_amount = fields.Monetary(
        string='Supplier invoice amount',  required=True)

    file = fields.Binary(
        "Document", required=True, attachment=True)

    file_name = fields.Char("File Name")

    purchase_orders_ids = fields.One2many(
        'document.line', 'document_id', string='Purchase Order')

    is_relationated_purchase_order = fields.Boolean(
        string='Is relationated to purchases orders', default=True)

    currency_id = fields.Many2one(string='Currency', readonly=True,
                                  related='purchase_orders_ids.currency_id')

    state = fields.Selection(string='Status',
                             selection=[
                                 ('draft', 'Draft'),
                                 ('confirmed', 'Confirmed'),
                                 ('invoiced', 'Invoiced')
                             ], required=True, readonly=True, default='draft')

    name_to_show = fields.Char(string='Document Filed Reference')

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code(
                'document.document')
        vals['name_to_show'] = '{} ({})'.format(
            vals['name'], vals['document_number'])
        return super().create(vals)

    def button_confirm(self):
        for document in self:
            if not document.is_relationated_purchase_order:
                self.write({'state': 'confirmed'})
                return True

            po_ids = []

            for purchase_order in document.purchase_orders_ids.filtered(lambda x: x.selected == True):
                po_ids.append((purchase_order.purchase_order_id,
                              purchase_order.status_settling))

            if not po_ids:
                raise ValidationError(
                    _("You must add purchases orders relationateds or deselect 'Is relationated to purchases orders'"))

            for purchase_order in po_ids:
                po_id, po_status_settling = purchase_order
                po = self.env['purchase.order'].search(
                    [('id', '=', po_id)])
                po.update({'status_settling': po_status_settling})

            self.write({'state': 'confirmed'})
            return True

    # def button_invoiced(self):
    #     self.write({'state': 'invoiced'})

    def update_state_invoiced(self):
        self.state = 'invoiced'
        return True

    @api.constrains('file')
    def _check_file(self):
        FILES_ALLOWED = ['pdf', 'jpg', 'jpeg', 'png', 'bmp']
        if str(self.file_name.split(".")[-1]) not in FILES_ALLOWED:
            raise ValidationError(
                "Cannot upload file different from PDF or IMAGE file")

    # @api.onchange("document_number")
    # def onchange_document_number(self):
    #     if self.document_number:
    #         self.name_to_show = f'{self.name} {self.document_number}'

    @api.onchange("partner_id")
    def onchange_partner(self):
        if self.partner_id:
            self.get_partner_purchase_orders()

    def get_partner_purchase_orders(self):
        purchase_orders = []
        self.write({"purchase_orders_ids": [(5, 0, 0)]})

        domain = [
            ("state", "in", ['purchase', 'done']),
            ("status_settling", "!=", "settled"),
            ("partner_id", "=", self.partner_id.id),
        ]
        purchase_orders_ids = self.env["purchase.order"].search(domain)
        for po in purchase_orders_ids:
            purchase_orders.append(
                {
                    "partner_id": po.partner_id.id,
                    "name": po.name,
                    "date_purchase_order": po.date_approve,
                    "amount_total": po.amount_total,
                    "purchase_order_id": po.id,
                    "currently_status_settling": po.status_settling
                }
            )
        self.purchase_orders_ids = [(0, 0, po) for po in purchase_orders]


class DocumentLine(models.TransientModel):
    _name = "document.line"
    _description = "Document Filed Line"

    document_id = fields.Many2one("document.document", "Document Filed")

    partner_id = fields.Many2one(
        "res.partner", string="Partner", readonly=True)

    currency_id = fields.Many2one(
        "res.currency", string="Currency", readonly=True)

    amount_total = fields.Monetary(string="Amount Total", readonly=True)

    name = fields.Char(string="Purchase Order Name", readonly=True)

    purchase_order_id = fields.Integer(string="Purchase Order Id")

    date_purchase_order = fields.Date(string="Invoice Date", readonly=True)

    status_settling = fields.Selection(
        string="Purchase Order Status Update",  selection=[
            ('partially_settled',
             'Partially Settled'),
            ('settled', 'Settled')
        ], required=True, default='partially_settled')

    currently_status_settling = fields.Selection(
        string="Currently Status",
        selection=[
            ('without_filing', 'Without Filing'),
            ('partially_settled',
             'Partially Settled'),
            ('settled', 'Settled')
        ], readonly=True)

    selected = fields.Boolean(default=False)

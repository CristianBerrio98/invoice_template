from odoo import models, fields, api

class AccountInvoice(models.Model):
    _inherit = 'account.move'
    _name = "account.invoice"

    transaction_ids_invoice = fields.Many2many('account.invoice', string='Transaction IDs')

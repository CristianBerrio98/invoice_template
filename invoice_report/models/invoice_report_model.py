from odoo import models, fields, api

class AccountInvoice(models.Model):
    _inherit = 'account.move'
    _name = "account.invoice"

from odoo import models, fields

class AccountInvoice(models.Model):
    _inherit = 'account.move'
    _name = "account.invoice"
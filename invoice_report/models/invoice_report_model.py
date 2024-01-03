from odoo import models, fields, api

class AccountInvoice(models.Model):
    _inherit = 'invoice_report.report_invoice_with_payments'

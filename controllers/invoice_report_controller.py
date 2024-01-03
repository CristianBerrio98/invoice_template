from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.main import ReportController

class ReportInvoiceWithPayments(ReportController):
    @http.route(['/report/pdf/module_name.report_invoice_with_payments/<int:docids>'], type='http', auth="user")
    def report_invoice_with_payments(self, docids, **data):
        report = request.env['ir.actions.report']._get_report_from_name('invoice_report_modulo.report_invoice_with_payments')
        docs = request.env['account.invoice'].browse(docids)
        pdf, _ = request.env.ref('invoice_report_modulo.report_invoice_with_payments').sudo()._render_qweb_pdf(docs.ids)
        pdfhttpheaders = [
            ('Content-Type', 'application/pdf'),
            ('Content-Length', len(pdf)),
            ('Content-Disposition', 'filename=Report_Invoice_With_Payments.pdf'),
        ]
        return request.make_response(pdf, headers=pdfhttpheaders)

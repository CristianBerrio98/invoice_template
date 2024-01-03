{
    'name': 'invoice_report',
    'description': """
        Get all TRM by date
    """,
    'author': "Cristian Berrio",
    'version': '1.0',
    'category': 'Invoice',
    'depends': ['base', 'account'],
    'data': [
        'views/report_invoice_with_payments.xml',
    ],
    'installable': True,
    'auto_install': False,
    'sequence': 1,
    'demo': [],
    'qweb': [
        'static/src/xml/module_name.xml',
    ],
}

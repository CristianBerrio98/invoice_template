{
    'name': 'Invoice Report Modulo',
    'version': '1.0',
    'category': 'Reports',
    'depends': ['base', 'account'],
    'data': [
        'views/report_invoice_with_payments.xml',
    ],
    'installable': True,
    'auto_install': True,
    'application': False,
    'sequence': 1,
    'demo': [],
    'qweb': [
        'static/src/xml/module_name.xml',
    ],
}

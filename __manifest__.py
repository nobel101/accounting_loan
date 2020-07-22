
{
    'name': 'Loan Accounting',
    'version': '12.0.1.0.0',
    'summary': ' Loan Accounting',
    'description': """
        Create accounting entries for loan requests.
        """,
    'category': 'Generic Modules/Human Resources',
    'author': "ERP graduation project 2020",
    'company': 'NCA Institution',
    'maintainer': 'NCA Institution',
    'depends': [
        'base', 'hr_payroll', 'hr', 'account', 'ohrms_loan',
    ],
    'data': [
        'views/hr_loan_config.xml',
        'views/hr_loan_acc.xml',

    ],
    'demo': [],
    'images': ['static/description/banner.jpg'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}

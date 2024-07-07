{
    'name': "MP Gestion",

    'summary': """Se agrega la gestion para la contabilidad""",
    'author': "Tonny Velazquez",
    'website': "corner.store59@gmail.com",
    'category': 'account',
    'version': '15.0.0.0.1',
    'depends': ['account', 'l10n_latam_invoice_document', 'payroll_payment', 'account_bank_cash_report'],
    'data': [
        # 'security/ir.model.access.csv',
        'security/mp_gestion_group.xml',
        'views/account_move_views.xml',
        # 'views/templates.xml',
    ],
    'license': 'Other proprietary',
}

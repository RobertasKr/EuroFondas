{
    'name': 'Library Management',
    'version': '1.0',
    'summary': 'Module for managing library books and loans',
    'author': 'Your Name',
    'depends': ['base', 'mail'],
    'data': [
        'data/cron.xml',
        'views/book_views.xml',
        'views/book_loan_views.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}

# -*- coding: utf-8 -*-
{
    'name': "hide_db_expired_message",
    'summary': "Hide the database has expired message",
    'description': """
        This module hides the "database has expired" message and prevents it from blocking the UI.
    """,
    'author': "My Company",
    'website': "https://www.yourcompany.com",
    'category': 'Custom',
    'version': '16.0.1.0.0',
    'depends': ['base', 'web'],
    'data': [
        # 'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_backend': [
            'hide_db_expired_message/static/src/js/hide_db_expired.js',
        ],
    },
    'installable': True,
    'application': False,
}

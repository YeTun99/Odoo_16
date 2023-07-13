# -*- coding: utf-8 -*-
{
    'name': "GCA Product  Summary Report",

    'summary': """
        Product Summary Report By Location""",

    'description': """
        Inventory Product Summary
    """,

    'author': "Global Connect Asia",
    'website': "http://www.gca.com.mm",
    'category': 'Inventory',
    'version': '1.1',
    # any module necessary for this one to work correctly
    'depends': ['base', 'stock'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

# -*- coding: utf-8 -*-
{
    'name': "Filter Management",
    'summary': "Control which fields appear in filters and group by for any model",
    'description': """
Filter Management module allows you to select a model and manage which fields appear
in the search filters and group by options in list/tree views. You can hide extra fields
and only show relevant ones for a cleaner UI and better reporting.
""",
    'version': '16.0.1',
    'sequence': 50,
    'author': "Muhammad Mubeen",
    'website': "https://www.linkedin.com/in/muhammad-mubeen-1601b12a7/",
    'license': 'LGPL-3',
	'support': 'mubeenodoo@gmail.com',
    'category': 'Tools',  # App store friendly category
    'price': 15.0,
    'currency': 'USD',

    # Dependencies
    'depends': [
        'base',
        'mail',
    ],

	'images': [
        'static/description/banner.png',
        'static/description/image_1.jpeg',
        'static/description/image_2.jpeg',
        'static/description/image_3.jpeg',
        'static/description/image_4.jpeg',
    ],

    # Data files loaded automatically
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],

    # Odoo App flags
    'installable': True,
    'application': True,
    'auto_install': False,
}
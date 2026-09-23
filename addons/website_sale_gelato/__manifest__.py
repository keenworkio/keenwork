# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "eCommerce/Gelato bridge",
    'category': 'Website/Website',
    'depends': ['sale_gelato', 'website_sale'],
    'data': [
        'data/delivery_carrier_data.xml',
    ],
    'installable': False,
    'auto_install': False,
    'author': 'Odoo S.A.',
    'license': 'LGPL-3',
}

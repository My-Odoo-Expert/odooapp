{
    'name': 'Analytic Account Inventory Operation',
    'version': '15.0.0.1.0.0',
    'summary': 'To assign analytic account to the operation transfer in inventory',
    'description': 'It will update all the related journal entry of that transfer',
    'category': 'Inventory',
    'price': "1.68",
    'currency': "USD",
    'author': 'OE Dev',
    'website': 'https://oe-dev.odoo.com/',
    'license': 'OPL-1',
    'depends': [
        'stock',
        'analytic'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/view_stock_picking_form_inherit.xml',
        'views/view_analytic_account_inventory_transfer_wizard.xml',
        'data/group_data.xml'
    ],
    'images': [
        'static/description/banner.png',
        'static/description/icon.png',
        'static/img/step1.png',
        'static/img/step2.png',
        'static/img/step3.png',
        'static/img/step4.png',
        'static/img/step5.png'
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'external_dependencies': {
        'python': [],
    }
}
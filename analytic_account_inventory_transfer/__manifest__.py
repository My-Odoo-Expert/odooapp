{
    'name': 'Analytic Account Inventory Operation',
    'version': '15.0.0.1.0.0',
    'summary': 'To assign analytic account to the operation transfer in inventory',
    'description': 'It will update all the related journal entry of that transfer',
    'category': 'Inventory',
    'author': 'OE',
    'website': 'www.oe.odoo.com',
    'license': '',
    'depends': [
        'stock',
        'analytic'
    ],
    'data': [
        'views/view_stock_picking_form_inherit.xml',
        'views/view_analytic_account_inventory_transfer_wizard.xml'
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'external_dependencies': {
        'python': [],
    }
}
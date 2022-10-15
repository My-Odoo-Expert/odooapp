from odoo import models, fields, api

class StockPickingInherit(models.Model):
    _inherit = 'stock.picking'

    x_analytic_account_id = fields.Many2one(comodel_name="account.analytic.account", string="Analytic Account", required=False)

    def open_analytic_account_wizard(self):
        for record in self:
            return{
                'name': 'Analytic Account',
                'type': 'ir.actions.act_window',
                'res_model': 'analytic.account.inventory.transfer.wizard',
                'view_id': self.env.ref('oe_analytic_account_inventory_transfer.view_analytic_account_inventory_transfer_wizard').id,
                'view_mode': 'form',
                'view_type': 'form',
                'target': 'new',
                'context': {
                    'default_x_stock_picking_id': record.id
                }
            }

from odoo import models, fields, api

class AnalyticAccountInventoryTransferWizard(models.TransientModel):
    _name = 'analytic.account.inventory.transfer.wizard'
    _description = 'The wizard to open model to setup analytic account'

    x_analytic_account_id = fields.Many2one(comodel_name="account.analytic.account", string="Analytic Account", required=True)
    x_stock_picking_id = fields.Many2one(comodel_name="stock.picking", string="Stock Picking", required=True)

    def apply_analytic_account_to_inventory_transfer(self):
        for record in self:
            stock_picking = self.env['stock.picking'].browse(record.x_stock_picking_id.id)
            if stock_picking:
                stock_picking.write({
                    'x_analytic_account_id': record.x_analytic_account_id.id
                })

            stock_moves = self.env['stock.move'].search([('picking_id', '=', record.x_stock_picking_id.id)])
            for stock_move in stock_moves:
                # Update stock move line of date to use force_date
                stock_move_lines = self.env['stock.move.line'].search([('move_id', '=', stock_move.id)])
                for stock_move_line in stock_move_lines:
                    stock_move_line.write({
                        'x_analytic_account_id': record.x_analytic_account_id.id
                    })
                # Update account move of date to use force_date
                account_moves = self.env['account.move'].search(
                    [('stock_move_id', '=', stock_move.id)])
                for account_move in account_moves:
                    # Update account move line of date to use force_date
                    account_move_lines = self.env['account.move.line'].search(
                        [('move_id', '=', account_move.id)])
                    for account_move_line in account_move_lines:
                        account_move_line.write({
                            'analytic_account_id': record.x_analytic_account_id.id
                        })
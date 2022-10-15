from odoo import models, fields, api

class StockMoveLineInherit(models.Model):
    _inherit = 'stock.move.line'

    x_analytic_account_id = fields.Many2one(comodel_name="account.analytic.account", string="Analytic Account", required=False)



from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    transaction_ids_move = fields.Many2many('account.invoice', string='Transaction IDs')
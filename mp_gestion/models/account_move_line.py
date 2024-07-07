from odoo import models, fields


class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    invoice_date = fields.Date(related='move_id.invoice_date')
    l10n_latam_document_type_id = fields.Many2one(related='move_id.l10n_latam_document_type_id')
    journal_id = fields.Many2one(related='move_id.journal_id')
    mp_flujo_id = fields.Many2one(related='move_id.mp_flujo_id')
    mp_grupo_flujo_ids = fields.Many2many(related="move_id.mp_grupo_flujo_ids")
    mp_grupo_flujo_id = fields.Many2one(related='move_id.mp_grupo_flujo_id')
    invoice_origin = fields.Char(related='move_id.invoice_origin')
    vat = fields.Char(related='move_id.partner_id.vat')
    code_account = fields.Char(related='account_id.code', string='Número de Cuenta Contable')

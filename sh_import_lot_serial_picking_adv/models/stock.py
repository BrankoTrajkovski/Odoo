# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import models

class StockPicking(models.Model):
    _inherit = "stock.picking"

    def action_import_lot_serial_adv(self):
        if self:
            action = self.env.ref(
                'sh_import_lot_serial_picking_adv.sh_import_lot_serial_adv_action').read()[0]
            return action
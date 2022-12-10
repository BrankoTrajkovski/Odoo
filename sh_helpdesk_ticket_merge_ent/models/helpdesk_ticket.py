# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from odoo import fields, models, _
from odoo.exceptions import UserError, ValidationError


class HelpdeskTicket(models.Model):
    _inherit = "helpdesk.ticket"

    merge_count = fields.Integer()
    child_ticket_id = fields.Many2one('helpdesk.ticket')

    def action_open_helpdesk_ticket_mrgd(self):
        childs = self.search(
            [('child_ticket_id', '=', self.id), ('active', '=', False)]).ids
        return {
            'name': _('Helpdesk Ticket'),
            'type': 'ir.actions.act_window',
            'view_type': 'list',
            'view_mode': 'list,form',
            'res_model': 'helpdesk.ticket',
            'domain': [('id', 'in', childs), ('active', '=', False)]
        }

    def import_data_manually_queue(self):

        view = self.env.ref(
            'sh_helpdesk_ticket_merge_ent.sh_merge_tickets_wizard')
        get_tickets = self.env['helpdesk.ticket'].browse(
            self.env.context.get('active_ids'))
        if len(get_tickets.ids) < 2:
            raise ValidationError(
                _('You should select minium two ticket for merge !!'))
        for tickets in self:
            for ticket in self:
                if ticket.partner_id != tickets.partner_id:
                    raise UserError(
                        _("You Can Only Merge Same Customers Tickets !!"))
        return {
            'name': 'Merge Tickets',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'views': [(view.id, 'form')],
            'res_model': 'sh.merge.tickets',
            'view_id': view.id,
            'target': 'new',
            'context': {'default_helpdesk_ticket_ids': self.ids,
                        'default_sh_partner_id': self.partner_id.id,
                        'default_helpdesk_team_id': self.team_id[0].id,
                        },
        }

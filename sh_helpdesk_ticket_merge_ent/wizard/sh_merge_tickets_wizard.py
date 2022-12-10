# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
from odoo import fields, models
from markupsafe import Markup, escape


class MergeWizard(models.TransientModel):
    _name = "sh.merge.tickets"
    _description = "Merge Helpdesk Ticekts"

    user_id = fields.Many2one(
        'res.users', 'Responsible User', default=lambda self: self.env.user)
    helpdesk_team_id = fields.Many2one('helpdesk.team', 'Support Team')
    sh_partner_id = fields.Many2one('res.partner', 'Customer')
    helpdesk_ticket_id = fields.Many2one('helpdesk.ticket', 'Support Ticket')
    create_new = fields.Boolean("Create New Ticket ?")
    merge_reason = fields.Char()
    helpdesk_ticket_ids = fields.Many2many(
        'helpdesk.ticket', string='Support Ticket', readonly="True")
    subject = fields.Char()

    def merge_select_tickets(self):
        if self.create_new:
            marged_disc = ''
            for desc in self.helpdesk_ticket_ids:
                if desc.description:
                    marged_disc = marged_disc + desc.name + escape(Markup("<hr/>")) + desc.description + escape(
                        Markup("<br/>")) if not desc.description == '<p><br></p>' else False
            dict = {
                'name': self.subject,
                'user_id': self.user_id.id,
                'team_id': self.helpdesk_team_id.id,
                'description': marged_disc,
                'partner_id': self.sh_partner_id.id,
            }
            self.env["helpdesk.ticket"].create(dict)

        elif self.helpdesk_ticket_id:

            mrgd_count = 0
            marged_disc = ''

            if self.helpdesk_ticket_id not in self.helpdesk_ticket_ids:
                if self.helpdesk_ticket_id.description:
                    marged_disc = self.helpdesk_ticket_id.description

            for desc in self.helpdesk_ticket_ids:
                if desc.description:
                    marged_disc = marged_disc + desc.name + escape(Markup("<hr/>")) + desc.description + escape(
                        Markup("<br/>")) if not desc.description == '<p><br></p>' else False
            self.helpdesk_ticket_id.description = marged_disc

            dict = {
                'user_id': self.user_id.id,
                'team_id': self.helpdesk_team_id.id,
            }
            for mrg_id in self.helpdesk_ticket_ids:
                mrg_id.child_ticket_id = self.helpdesk_ticket_id.id
                if mrg_id != self.helpdesk_ticket_id:
                    mrg_id.action_archive()
                    mrgd_count += 1
            self.helpdesk_ticket_id.merge_count = mrgd_count
            self.helpdesk_ticket_id.write(dict)

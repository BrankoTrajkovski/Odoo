# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    'name': 'Merge Helpdesk Support Tickets',
    "author": "Softhealer Technologies",
    'version': '16.0.1',
    "license": "OPL-1",
    "website": "https://www.softhealer.com",
    'category': 'Discuss',
    "support": "support@softhealer.com",
    'summary': 'Merge Helpdesk Ticket Merge Helpdesk Support Tickets Merge Tickets Support Ticket Merge Tickets Of Helpdesk Support System Merge support Issues Merge Multiple Tickets Merge Support Ticket Combine Support Ticket Odoo',
    'description': """When there is the same support ticket of same client it's easy to merge them using this module. You can merge tickets as well as create a new ticket while merging ticket.""",
    'depends': ['base_setup', 'helpdesk'],
    'data': [
        "security/ir.model.access.csv",
        "views/helpdesk_ticket_views.xml",
        "wizard/merge_wizard_views.xml",
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    "images": ["static/description/background.png", ],
    "price": 30,
    "currency": "EUR"
}

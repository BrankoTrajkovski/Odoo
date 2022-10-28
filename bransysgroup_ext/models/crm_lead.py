# -*- coding: utf-8 -*-
# Part of Synconics. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class CRMLead(models.Model):
    _inherit = 'crm.lead'

    x_DOT = fields.Integer('DOT Number', help="DOT number of the company")
    x_MC = fields.Char('MC number', help="Motor Carrier Number issued by FMCSA")
    x_NumberOfAssets = fields.Integer('Number of assets')
    x_Trucks = fields.Integer('Number Of Trucks')
    x_CarrierRating = fields.Char('Carrier Rating')
    x_HOSCOMPPCT = fields.Float('HOS Compliance Score')
    x_UNSAFEDRIVPCT = fields.Float('Unsafe Driving Score')
    x_ScoreDate = fields.Datetime('Last Score Update')
    x_CargoType = fields.Selection([('GP', 'General Property'), ('WM', 'Waste Management'),
        ('LV', 'Light Vehicles')], string="Cargo Type")


class ResPartner(models.Model):
    _inherit = 'res.partner'

    x_DOT = fields.Integer('DOT Number', help="DOT number of the company")
    x_MC = fields.Char('MC number', help="Motor Carrier Number issued by FMCSA")

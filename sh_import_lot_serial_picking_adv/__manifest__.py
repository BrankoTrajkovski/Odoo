# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Import Lot-Serial Picking From CSV-Excel File - Advance | Import Lot From CSV File | Import Lot From Excel File | Import Serial From CSV File | Import Serial From Excel File",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "version": "16.0.1",
    "category": "Warehouse",
    "license": "OPL-1",
    "summary": "Import lot picking From CSV Import lot picking from Excel Import serial picking from csv Import serial picking from Excel import picking from XLS Import pickings From XLSX Import Serial Number import Lot Number import lot serial in picking Odoo",
    "description": """Sometimes it's time wasting process while importing lots/serial number when products received and delivered. This module imports lot/serial picking from CSV/Excel files in a single click. You can import lot/serial number in multiple products. Import multiple products lot/serial will make whole process simple and fast.""",
    "depends": [
        'stock',
        'sh_message',
    ],
    "data": [
        'security/import_lot_security.xml',
        'security/ir.model.access.csv',
        'wizard/import_lot_wizard_views.xml',
        'views/stock_views.xml',
    ],
    "images": ["static/description/background.png", ],
    "installable": True,
    "auto_install": False,
    "application": True,
    "price": "40",
    "currency": "EUR"
}

# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# List of contributors:
# Marc Tormo <marc@batista10.cat>

{
    "name" : "Andorra - Accounting",
    "version" : "0.1",
    "author" : "Batista10",
    'category': 'Localization',
    "description": """
Andorra Comptes Comptables 
==========================

    * Creació de grups comptables
    * Creació del Pla General Comptable
    * Creació de taxes Andorranes (IGI, IRPF)
""",
    "depends" : [
        "account",
        "base_iban",
        "base_vat",
    ],
    "data" : [
        'data/account_group.xml',
        'data/account_chart_template_data.xml',
        'data/account.account.template-common.csv',
        'data/account.account.template-full.csv',
        'data/account_chart_template_account_account_link.xml',
        'data/account_data.xml',
        'data/account_tax_data.xml',
        'data/account_fiscal_position_template_data.xml',
        'data/account_chart_template_configure_data.xml',
    ],
}

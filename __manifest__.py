# pylint: disable=missing-module-docstring,pointless-statement
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "POS Webhook Sender",
    "summary": "Envía datos de órdenes POS a un webhook si el cliente tiene número móvil.",
    "author": "Be OnlyOne",
    "maintainers": ["onlyone-odoo"],
    "website": "https://onlyone.odoo.com/",
    "license": "AGPL-3",
    "category": "Sales/Point of Sale",
    "version": "16.0.1.0.0",
    "development_status": "Production/Stable",
    "application": False,
    "installable": True,
    "external_dependencies": {
        "python": [],
        "bin": [],
    },
    "depends": ["base_automation", "point_of_sale"],
    "data": [
        "data/automated_actions.xml",
    ],
}

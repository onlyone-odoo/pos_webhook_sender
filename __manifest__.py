# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "POS Webhook Sender",
    "summary": "Sends POS order data to a webhook if the customer has a mobile number.",
    "author": "Be OnlyOne",
    "maintainers": ["onlyone-odoo"],
    "website": "https://onlyone.odoo.com/",
    "license": "AGPL-3",
    "category": "Sales/Point of Sale",
    "version": "16.0.2.1.0",
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

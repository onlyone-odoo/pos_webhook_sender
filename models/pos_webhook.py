from odoo import models, _
import requests
import json
import logging

_logger = logging.getLogger(__name__)


class PosOrder(models.Model):
    _inherit = "pos.order"

    def send_to_webhook(self):
        """Send order data to the webhook if the customer has a mobile number."""
        webhook_url = "https://hook.us2.make.com/aygs50eqg8xnziaw3w0pdfhng1rqy6ry"
        for record in self:
            partner = record.partner_id
            # Check if the customer has a mobile number
            if not partner or not partner.mobile:
                _logger.info(_("Webhook not sent: customer has no mobile number."))
                return
            # Prepare data in JSON format
            data = {
                "full_name": partner.name or _("Customer without name"),
                "mobile_number": partner.mobile,
                "purchase_mode": "local",
                "purchase_location": record.config_id.name or _("No POS config"),
                "email": partner.email or "",
            }
            # Send data to the webhook
            try:
                response = requests.post(webhook_url, json=data, timeout=10)
                response.raise_for_status()
                _logger.info(_("Data successfully sent to webhook."))
            except Exception as e:
                _logger.error(_("Error sending to webhook: %s") % str(e))

from odoo import models
import requests
import json
import logging

_logger = logging.getLogger(__name__)


class PosOrder(models.Model):
    _inherit = "pos.order"

    def send_to_webhook(self):
        """Envía los datos de la orden al webhook si el cliente tiene número móvil."""
        webhook_url = "https://hook.us2.make.com/aygs50eqg8xnziaw3w0pdfhng1rqy6ry"
        for record in self:
            partner = record.partner_id
            # Verificar si el cliente tiene número móvil
            if not partner or not partner.mobile:
                _logger.info("No se envía al webhook: cliente sin número móvil.")
                return
            # Preparar los datos en formato JSON
            data = {
                "full_name": partner.name or "Cliente sin nombre",
                "mobile_number": partner.mobile,
                "purchase_mode": "local",
                "purchase_location": record.config_id.name or "Sin caja",
                "email": partner.email or "",
            }
            # Enviar al webhook
            try:
                response = requests.post(webhook_url, json=data, timeout=10)
                response.raise_for_status()
                _logger.info("Datos enviados al webhook con éxito.")
            except Exception as e:
                _logger.error("Error enviando al webhook: %s" % str(e))

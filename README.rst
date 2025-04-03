===========
POS Webhook Sender
===========

.. |badge1| image:: https://img.shields.io/badge/maturity-Stable-brightgreen
    :target: https://odoo-community.org/page/development-status
    :alt: Stable
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://onlyone.odoo.com/web/image/website/1/logo/OnlyOne%20Soft?unique=dccda5b
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3

|badge1| |badge2| |badge3| 

This module extends the functionality of Odoo Point of Sale to support sending order data to a webhook when a POS order is created, provided the customer has a mobile number registered, and to allow you to integrate with external systems seamlessly.

**Table of contents**

.. contents::
   :local:

Install
=======

To install this module, you need to:

1. Place the module folder `pos_webhook_sender` in your Odoo addons directory.
2. Update the module list in Odoo (Apps > Update Apps List).
3. Search for "POS Webhook Sender" in the Apps menu and click "Install".

Usage
=====

1. Go to the Point of Sale module and create a new POS order.
2. Ensure the customer associated with the order has a mobile number registered.
3. Upon order creation, the module will automatically send a JSON payload to the configured webhook with the customer’s full name, mobile number, purchase mode, purchase location (POS config name), and email (if available).

Known issues / Roadmap
======================

* Currently, the webhook URL is hardcoded in the module. Future versions may include a configuration setting for the URL.

Bug Tracker
===========

* For support, contact us at <https://onlyone.odoo.com/contactus>.

Credits
=======

Authors
~~~~~~~

* Be OnlyOne

Contributors
~~~~~~~~~~~~

* `Be OnlyOne. <https://onlyone.odoo.com/>`_
  
  * Matías Bressanello

Maintainers
~~~~~~~~~~~

This module is maintained by Be OnlyOne 
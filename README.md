# Frappe 3PL Multi-Client Warehouse Billing Engine

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![3PL](https://img.shields.io/badge/Supply%20Chain-3PL%20WMS-teal.svg)](https://frappe.io)

Activity-Based Costing (ABC) engine for third-party logistics (3PL) multi-client warehouses, calculating pallet-day storage, cross-docking, pick-pack fulfillment, and value-added service fees.

## Features
- **Pallet-Day Billing:** Accurate daily occupancy meters accounting for inbound arrival and outbound dispatch times.
- **Contract-Specific Tariffs:** Custom handling rates per client contract with automated surcharge brackets.
- **GST Compliant Invoicing:** Consolidated monthly billing statement with service-wise SAC code breakdowns.

## Tests
```bash
python3 -m unittest discover tests
```

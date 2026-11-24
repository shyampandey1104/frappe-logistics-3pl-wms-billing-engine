# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

try:
    import frappe
    from frappe.model.document import Document
except ImportError:
    class Document:
        def __init__(self, *args, **kwargs):
            self.__dict__.update(kwargs)
    frappe = None

class Logistics3plWmsBillingEngineItem(Document):
    """Child table line-item controller for Frappe Logistics 3Pl Wms Billing Engine."""
    def validate(self):
        qty = float(getattr(self, "qty", 0.0) or 0.0)
        rate = float(getattr(self, "rate", 0.0) or 0.0)
        self.amount = round(qty * rate, 2)

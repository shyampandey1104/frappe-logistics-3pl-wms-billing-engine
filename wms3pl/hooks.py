# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "wms3pl"
app_title = "Frappe Logistics 3Pl Wms Billing Engine"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Logistics 3Pl Wms Billing Engine for Frappe and ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/wms3pl/css/wms3pl.bundle.css"
app_include_js = "/assets/wms3pl/js/wms3pl.bundle.js"

# Document Events
# ---------------
doc_events = {
    "DocType Event": {
        "on_submit": "wms3pl.engine.on_document_submit",
        "on_cancel": "wms3pl.engine.on_document_cancel"
    }
}

# Scheduled Tasks
# ---------------
scheduler_events = {
    "daily": [
        "wms3pl.engine.daily_scheduled_sync"
    ]
}

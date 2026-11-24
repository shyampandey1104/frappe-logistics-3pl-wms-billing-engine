# Copyright (c) 2026, Shyamkumar Pandey and contributors
# For license information, please see license.txt

app_name = "wms3pl"
app_title = "Frappe Logistics 3Pl Wms Billing Engine"
app_publisher = "Shyamkumar Pandey"
app_description = "Frappe Logistics 3Pl Wms Billing Engine - Enterprise Multi-DocType Solution for Frappe & ERPNext"
app_email = "shyampandey1104@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------
app_include_css = "/assets/wms3pl/css/wms3pl.bundle.css"
app_include_js = "/assets/wms3pl/js/wms3pl.bundle.js"

# Document Events
# ---------------
doc_events = {
    "Frappe Logistics 3Pl Wms Billing Engine Entry": {
        "validate": "wms3pl.services.validator.EnterpriseValidationEngine.validate_compliance_rules",
        "on_submit": "wms3pl.services.integration_service.EnterpriseIntegrationService.verify_remote_status"
    }
}

# Scheduled Background Tasks
# --------------------------
scheduler_events = {
    "hourly": [
        "wms3pl.tasks.hourly_sync"
    ],
    "daily": [
        "wms3pl.tasks.daily_reconciliation"
    ],
    "weekly": [
        "wms3pl.tasks.weekly_digest"
    ]
}

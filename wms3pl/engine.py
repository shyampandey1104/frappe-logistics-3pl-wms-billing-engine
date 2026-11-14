"""Third-Party Logistics (3PL) Multi-Client Activity & Storage Billing Engine."""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass, field


@dataclass
class ClientSLAContract:
    client_id: str
    client_name: str
    rate_per_pallet_day: float = 12.0
    inbound_unload_rate_per_pallet: float = 35.0
    outbound_pick_pack_rate_per_order: float = 25.0
    shrink_wrap_rate_per_pallet: float = 40.0


@dataclass
class Monthly3PLInvoice:
    invoice_number: str
    client_id: str
    client_name: str
    pallet_storage_charge: float
    inbound_handling_charge: float
    outbound_handling_charge: float
    value_added_services_charge: float
    gross_bill_amount: float
    tax_gst_18pct: float
    total_payable: float


class Logistics3PLBillingEngine:
    """Calculates multi-tenant 3PL warehouse logistics charges and monthly SLA client billing."""

    def generate_monthly_invoice(
        self,
        invoice_no: str,
        contract: ClientSLAContract,
        total_pallet_days_held: int,
        inbound_pallets_received: int,
        outbound_orders_fulfilled: int,
        pallets_shrink_wrapped: int
    ) -> Monthly3PLInvoice:
        storage_charge = round(total_pallet_days_held * contract.rate_per_pallet_day, 2)
        inbound_charge = round(inbound_pallets_received * contract.inbound_unload_rate_per_pallet, 2)
        outbound_charge = round(outbound_orders_fulfilled * contract.outbound_pick_pack_rate_per_order, 2)
        vas_charge = round(pallets_shrink_wrapped * contract.shrink_wrap_rate_per_pallet, 2)

        gross = round(storage_charge + inbound_charge + outbound_charge + vas_charge, 2)
        gst = round((gross * 18.0) / 100.0, 2)
        net_total = round(gross + gst, 2)

        return Monthly3PLInvoice(
            invoice_number=invoice_no,
            client_id=contract.client_id,
            client_name=contract.client_name,
            pallet_storage_charge=storage_charge,
            inbound_handling_charge=inbound_charge,
            outbound_handling_charge=outbound_charge,
            value_added_services_charge=vas_charge,
            gross_bill_amount=gross,
            tax_gst_18pct=gst,
            total_payable=net_total
        )

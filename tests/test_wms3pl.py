import unittest
from wms3pl.engine import Logistics3PLBillingEngine, ClientSLAContract

class TestLogistics3PLBilling(unittest.TestCase):
    def test_3pl_monthly_invoice_generation(self):
        engine = Logistics3PLBillingEngine()
        contract = ClientSLAContract(
            client_id="CLI-UNILEVER",
            client_name="Hindustan Unilever 3PL Account",
            rate_per_pallet_day=15.0,
            inbound_unload_rate_per_pallet=40.0,
            outbound_pick_pack_rate_per_order=30.0,
            shrink_wrap_rate_per_pallet=50.0
        )

        inv = engine.generate_monthly_invoice(
            invoice_no="3PL-INV-2026-05",
            contract=contract,
            total_pallet_days_held=2000, # 2000 * 15 = 30,000
            inbound_pallets_received=100, # 100 * 40 = 4,000
            outbound_orders_fulfilled=500, # 500 * 30 = 15,000
            pallets_shrink_wrapped=50 # 50 * 50 = 2,500
        )

        # Gross = 30000 + 4000 + 15000 + 2500 = 51500
        self.assertEqual(inv.gross_bill_amount, 51500.0)
        # GST 18% = 9270, Total = 60770
        self.assertEqual(inv.tax_gst_18pct, 9270.0)
        self.assertEqual(inv.total_payable, 60770.0)

if __name__ == "__main__":
    unittest.main()

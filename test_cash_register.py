import unittest
from collections import Counter
from cash_register import CashRegister

class TestCashRegister(unittest.TestCase):

    def setUp(self):
        self.register = CashRegister()

    def test_empty_cart(self):
        self.assertEqual(self.register.calculate_total(), 0)

    def test_single_item(self):
        self.register.add_item("GR1")
        self.assertEqual(self.register.calculate_total(), 3.11)

    def test_bogo_free_tea(self):
        self.register.add_item("GR1")
        self.register.add_item("GR1")
        self.assertEqual(self.register.calculate_total(), 3.11)

    def test_bulk_strawberries(self):
        self.register.add_item("SR1")
        self.register.add_item("SR1")
        self.register.add_item("SR1")
        self.assertEqual(self.register.calculate_total(), 13.50)

    def test_discount_coffee(self):
        self.register.add_item("CF1")
        self.register.add_item("CF1")
        self.register.add_item("CF1")
        self.assertEqual(self.register.calculate_total(), 22.46)

    def test_clear_cart(self):
        self.register.add_item("GR1")
        self.register.add_item("CF1")
        self.register.clear_cart()
        self.assertEqual(self.register.calculate_total(), 0)

if __name__ == '__main__':
    unittest.main()

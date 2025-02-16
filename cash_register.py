import tkinter as tk
from collections import Counter
import unittest

class CashRegister:
    PRICES = {"GR1": 3.11, "SR1": 5.00, "CF1": 11.23}

    def __init__(self):
        self.cart = Counter()

    def add_item(self, item):
        self.cart[item] += 1

    def clear_cart(self):
        self.cart.clear()

    def calculate_total(self):
        count = self.cart
        total = 0

        if count["GR1"] > 0:
            total += (count["GR1"] // 2 + count["GR1"] % 2) * self.PRICES["GR1"]

        if count["SR1"] >= 3:
            total += count["SR1"] * 4.50
        else:
            total += count["SR1"] * self.PRICES["SR1"]

        if count["CF1"] >= 3:
            total += count["CF1"] * (self.PRICES["CF1"] * 2 / 3)
        else:
            total += count["CF1"] * self.PRICES["CF1"]

        return round(total, 2)

def create_ui():
    register = CashRegister()

    def add_item(item):
        register.add_item(item)
        cart_label.config(text=f"Cart: {dict(register.cart)}")

    def show_total():
        total_label.config(text=f"Total: €{register.calculate_total()}")

    def clear_cart():
        register.clear_cart()
        cart_label.config(text="Cart: {}")
        total_label.config(text="Total: €0.00")

    root = tk.Tk()
    root.title("Cash Register")

    tk.Label(root, text="Select a product:").pack()

    for product, price in CashRegister.PRICES.items():
        tk.Button(root, text=f"{product} - €{price}", command=lambda p=product: add_item(p)).pack()

    cart_label = tk.Label(root, text="Cart: {}")
    cart_label.pack()

    tk.Button(root, text="Clear Cart", command=clear_cart).pack()  # Pulsante per svuotare il carrello
    tk.Button(root, text="Calculate Total", command=show_total).pack()

    total_label = tk.Label(root, text="Total: €0.00")
    total_label.pack()

    root.mainloop()

if __name__ == "__main__":
    create_ui()

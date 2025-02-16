# test_Amenitiz
# Cash Register

## Overview
This project implements a simple yet effective **cash register system** that allows users to:
- **Scan products** and add them to a cart
- **Apply discounts and pricing rules** automatically
- **Calculate the total price**
- **Clear the cart** when needed

It includes both **frontend (Tkinter UI)** and **backend (pricing logic with TDD)** in a single Python file for simplicity.

---

## Features
✅ **Usable & Simple**:
- A straightforward user interface (UI) using **Tkinter**.
- Only essential features are included to keep the UX intuitive.
- No external dependencies apart from the Python standard library.

✅ **Readable & Maintainable**:
- Code is modular, with each function having a clear responsibility.
- The `CashRegister` class encapsulates all business logic.
- UI logic is kept separate from pricing rules.

✅ **Easily Extendable**:
- New products and pricing rules can be added easily.
- The logic is structured in a way that supports future expansions.
- Additional UI enhancements (e.g., product images) can be integrated with minimal changes.

---

## Installation & Usage

### Prerequisites
- Python 3.7 or later

### Run the Cash Register UI
```sh
python cash_register.py
```
This will open a simple UI where you can:
- Click buttons to add products
- View the cart contents
- Calculate the total
- Clear the cart

### Running the Unit Tests
To ensure the logic is working correctly, run:
```sh
python -m unittest test_cash_register.py
```

This will execute a set of test cases verifying:
- Correct price calculations
- Discounts applied properly
- The clear cart functionality

---

## Code Structure
```
/cash_register
│── cash_register.py  # Contains both backend logic and UI
│── test_cash_register.py  # Unit tests following TDD principles
```

### Main Components
1. **CashRegister Class** (Backend)
   - Handles product pricing and discount rules
   - Supports adding/removing products and clearing the cart
   - Implements `calculate_total()` for price computation

2. **Tkinter UI** (Frontend)
   - Provides a user-friendly interface to interact with the system
   - Buttons to add products, calculate total, and clear the cart
   
3. **Unit Tests**
   - Ensures correctness of pricing logic with different scenarios
   - Validates business rules like "Buy One Get One Free" and bulk discounts

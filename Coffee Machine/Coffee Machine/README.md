# ☕ Coffee Machine Simulator (Python CLI)

A simple terminal-based coffee machine simulation written in Python.  
It allows users to order drinks, manage resources, and simulate coin transactions—just like a real coffee vending machine!

---

## 📋 Features

- ✅ Supports three drinks: **Espresso**, **Latte**, and **Cappuccino**
- 💰 Accepts virtual coins: penny, dime, nickel, quarter
- 📉 Deducts ingredients based on the order
- 📈 Generates a resource and profit report
- 🧠 Built using dictionaries, functions, and loops
- 🚨 Checks for insufficient ingredients or money

---

## 🧪 How It Works

1. User is prompted to choose: `espresso`, `latte`, `cappuccino`, or `report`
2. If ingredients are enough:
   - Proceeds to ask for money
   - Calculates total and compares with drink cost
   - Returns change (if any) and deducts resources
3. If not enough resources or money:
   - Gives a warning
   - Cancels the transaction

---

## 🛠️ Requirements

No external libraries needed.  
Just pure Python. Compatible with Python 3.7 and above.

---

## 🧾 Sample Output

```shell
What would you like? cappuccino, latte, or espresso?
> latte

Insert your coins here:
Penny: 10
Dime: 10
Nickel: 5
Quarter: 5

Here, your latte ☕
Your change is 0.3

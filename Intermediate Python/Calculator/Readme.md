# 🧮 Terminal-Based Python Calculator

A simple, interactive calculator written in **Python**, designed for the command line. It performs **basic arithmetic operations** and allows **continuous calculations** using the result of the previous operation.

---

## 🚀 Features

- Supports the four fundamental operations:
  - ➕ Addition
  - ➖ Subtraction
  - ✖️ Multiplication
  - ➗ Division
- Continues calculation using the previous result
- Clears the screen when starting a new calculation
- Designed for both Windows and Unix-based terminals

---

## 📂 Project Structure


---

## 🧠 How It Works

1. User inputs the **first number**.
2. User selects an **operation** (`+`, `-`, `*`, `/`).
3. User provides the **second number**.
4. Program performs the operation and displays the result.
5. User can:
   - Type `y` to **continue** using the result as the new first number.
   - Type `n` to **clear the screen** and start fresh with a new number.

---

## 📦 Requirements

- Python 3.x

No external libraries are required. The code only uses Python’s built-in `os` module.

---

## 🛠️ How to Run

1. Clone the repository or copy the code into a file named `calculator.py`.
2. Open a terminal and navigate to the directory.
3. Run the script with:

```bash
python calculator.py

WHat s the first number= 10
What operation you want
+
-
*
/
+
Write the second number = 5
Your calculated number is 15
Do you want to continue with this number if yes type y if not type n: y

What operation you want
+
-
*
/
*
Write the second number = 2
Your calculated number is 30

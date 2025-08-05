# 🏆 Secret Auction Program (Python)

This project is a **command-line-based auction simulator** that allows multiple users to place their bids anonymously. At the end of the bidding process, the program determines and announces the highest bidder.

## 💡 Features

- Accepts multiple bids from different users
- Keeps all bids **confidential** until the end
- Automatically clears the screen after each bid (supports Windows & Unix)
- Identifies and announces the **highest bidder**

---

## 📌 How It Works

1. Each user is prompted to enter their name and bid amount.
2. After each bid, the screen clears to maintain **privacy**.
3. Once there are no more bidders, the program:
   - Loops through the stored bids
   - Determines the highest bid
   - Announces the winner

---

## 🛠️ Technologies Used

- **Python 3**
- Standard library: `os` (for screen clearing)

---

## 🚀 Getting Started

1. **Clone the repo** or copy the code into your IDE
2. Run the script:
   ```bash
   python auction.py

## 🛠️ Sample Output

What is your name? Alice\
What is your bid? 120\
Do you have another bider: yes

What is your name? Bo\b
What is your bid? 150\
Do you have another bider: no\

tyhe winner is Bob with a bid of 150

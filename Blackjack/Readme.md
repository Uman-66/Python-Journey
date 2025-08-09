# 🃏 Blackjack Game in Python

A simple command-line Blackjack game where you play against the computer.

## 🎯 Features

* Deal initial 2 cards to player and computer
* Option to draw more cards or hold
* Automatic Ace value adjustment (11 → 1) if score exceeds 21
* Clear terminal between rounds
* Play multiple rounds in a single run

## 🛠️ Technologies Used

* Python 3
* `random` module for card drawing
* `os` module for clearing the screen

## 📜 How to Play

1. The game starts with 2 cards each for you and the computer.
2. You will see your hand and one of the computer's cards.
3. Choose:

   * `yes` → draw another card
   * `no` → hold and let the computer play
4. The closest to 21 without going over wins.

## ▶️ How to Run

```bash
# Clone the repository
git clone https://github.com/yourusername/blackjack-game.git

# Navigate into the project folder
cd blackjack-game

# Run the game
python blackjack.py
```

## 📌 Example Gameplay

```
Your cards are [10, 7]
Computer's first card is 8
Do you want to add a new card? yes if u want to hold no. yes
Your new cards are [10, 7, 2]
Do you want to add a new card? yes if u want to hold no. no
You win!!!!!!!!!!!!!
```

## 💡 Future Improvements

* Add betting system with virtual chips
* Improve computer's decision-making logic
* Add card deck depletion for realism

## 📄 License

This project is open-source and available under the MIT License.

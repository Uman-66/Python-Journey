# 🐍 Snake Game in Python (Turtle Graphics)

A classic **Snake Game** implemented using Python's built-in `turtle` module.
Eat food, grow your snake, and try not to crash into the walls or yourself!

---

## 📌 Features

* Smooth snake movement using keyboard controls
* Randomly generated food locations
* Scoreboard that updates in real-time
* Game-over detection when:

  * Snake hits a wall
  * Snake runs into itself
* Simple, clean OOP structure:

  * `Snake` class → handles movement & growth
  * `Food` class → handles random placement
  * `ScoreBoard` class → handles score display

---

## 🚀 Getting Started

### Prerequisites

* Python 3.6 or newer
* No external libraries — uses Python’s built-in `turtle` module

### Installation

Clone the repository and navigate to the folder:

```bash
git clone https://github.com/uman66/snake-game.git
cd snake-game
```

---

## ▶️ How to Play

Run the main script:

```bash
python main.py
```

Controls:

* **Up Arrow** → Move Up
* **Down Arrow** → Move Down
* **Left Arrow** → Move Left
* **Right Arrow** → Move Right

Rules:

* Eat purple food to grow longer and earn points
* Avoid hitting the walls
* Avoid running into yourself

---

## 📂 Project Structure

```
snake-game/
│
├── main.py         # Main game loop
├── snake.py        # Snake class
├── food.py         # Food class
└── scoreboard.py   # ScoreBoard class
```

---

## 🛠 Possible Improvements

* Add difficulty levels (speed increase as score rises)
* Save high scores to a file
* Add background music and sound effects
* Create a start menu and restart option

---

## 📜 License

This project is licensed under the MIT License.

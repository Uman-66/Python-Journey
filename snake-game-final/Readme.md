# 🐍 Advanced Snake Game

An upgraded version of the classic Snake Game built with Python's `turtle` module. This version includes persistent high scores, smooth collision detection, and game reset functionality.

---

## 📊 Features

* **Persistent High Score:** Tracks and stores the highest score in a text file.
* **Snake Growth:** Snake grows longer when it eats food.
* **Collision Detection:** Detects collisions with walls and the snake's own body.
* **Game Reset:** Automatically resets the game upon collision without closing the window.
* **Color-Coded Elements:** Distinct snake, food, and scoreboard visuals.

---

## 🚀 Getting Started

### Prerequisites

* Python 3.6 or later installed on your system.

### Installation

1. Clone the repository:

```bash
git clone https://github.com/uman66/advanced-snake-game.git
cd advanced-snake-game
```

2. Make sure `data.txt` exists in the same directory for high score tracking.

   * Example:

```text
0
```

---

## ▶️ How to Play

1. Run the game:

```bash
python main.py
```

2. Control the snake using **Arrow Keys**:

   * **Up** ↑
   * **Down** ↓
   * **Left** ←
   * **Right** →
3. Eat the blue food to increase your score and grow the snake.
4. Avoid hitting walls or your own tail.

---

## ⚖️ File Structure

```
advanced-snake-game/
|— main.py            # Game loop and core logic
|— snake.py           # Snake movement and growth logic
|— food.py            # Food creation and refresh
|— scoreboard.py      # Score tracking and high score persistence
|— data.txt           # High score storage file
```

---

## ⚠️ Notes

* Ensure `data.txt` path in `scoreboard.py` is correct for your system.
* The game uses `turtle` graphics, so performance may vary depending on the system.

---

## 🛠 Possible Improvements

* Add difficulty levels.
* Implement a start/restart menu.
* Add background music and sound effects.

---

## 📜 License

This project is licensed under the MIT License.

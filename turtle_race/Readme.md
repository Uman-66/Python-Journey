# 🐢 Turtle Race Game

A fun, interactive turtle race game built with Python’s built-in `turtle` graphics module. Pick a turtle color, watch them race, and see if your pick wins!

---

## 🎮 How It Works

- The game opens a turtle graphics window with 6 turtles in rainbow colors.
- You are prompted to **guess** which turtle (color) will win.
- Turtles move randomly forward in a race.
- If your guessed turtle wins, you get a congratulatory message in the terminal.

---

## 🧠 Game Logic

- Each turtle moves forward by a random distance between `1` and `10` units per loop.
- The first turtle to cross the finish line (x > 230) wins.
- User guess is compared with the winning turtle's color.

---

## 📂 Project Files

```bash
📁 turtle-race-game/
├── main.py       # Contains full game logic
├── README.md     # Documentation
```

---

## 📸 Sample Output

```text
Guess who will win?
Choose any colour from the rainbow: green

Congratulations! You won! green won the race
```

_or_

```text
Sorry, you lose. red won the race
```

---

## 🛠️ Requirements

- Python 3.6+
- No external libraries
- Works on all operating systems

---

## 🚀 How to Run

```bash
python main.py
```

---

## 🌈 Colors Used

- purple
- blue
- green
- yellow
- orange
- red

> You must type your color guess exactly as above (case-insensitive is recommended to add in future).

---

## 🧹 Possible Improvements

- Normalize user input (make it case-insensitive)
- Add replay option
- Track win/loss history
- Add a countdown before the race

---

## 👩‍💻 Author

Made with love using `turtle` graphics 🐢  
By Uman
---

## 📜 License

This project is open-source and free to use under the [MIT License](LICENSE).


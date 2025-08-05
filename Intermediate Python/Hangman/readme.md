# 🎯 Day 8 – Hangman Game (Python)

Welcome to Day 8 of my Python learning journey!  
This is a classic **Hangman game** implementation in Python, where the player must guess letters in a hidden word before running out of lives. Each incorrect guess brings the player closer to the *ASCII-art doom*!

---

## 🧠 Features

- Random word selection from a word list.
- Visual lives tracking via ASCII art (`draw.py`).
- Case-insensitive guessing.
- Dynamic word reveal as letters are guessed.
- End-game handling (win/lose with word reveal).

---

## 📂 Project Structure


---

## 🎮 How to Play

1. Run the `hangman.py` file.
2. You'll see underscores representing the hidden word.
3. Guess letters one at a time.
4. Each wrong guess costs one life. Lose all lives = game over!
5. Guess the full word correctly before lives run out to win.

---

## 🔧 Requirements

No external libraries needed. Just pure Python.

- Python 3.x
- `draw.py` must be in the same directory as `hangman.py`

---

## ✨ Sample Output


---

## 📜 Notes

- The current word list is small (`["aardvark", "baboon", "camel"]`), but can be easily extended.
- ASCII art is stored in `draw.py` as a list of strings (`stages[]`).
- Error handling is basic — this is a beginner-friendly version!

---

## 🚀 What I Learned

- Working with lists and indices.
- `for` loops and conditional logic.
- String comparisons and updates.
- Modular file imports.
- Game design logic in CLI environments.

---

## 💭 Future Enhancements

- Add difficulty levels (easy/medium/hard word sets).
- Track and display guessed letters so far.
- GUI version using `tkinter`.
- Multiplayer mode (pass-the-keyboard style).
- Add sound feedback using `pygame`.

---

##  About This Repo

This project is part of my public Python journey repo – documenting daily learning with clean, working examples.  
Follow along or fork it to grow your own journey ✨

---

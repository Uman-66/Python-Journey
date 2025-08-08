# 🔼 Higher Lower Game (Instagram Followers Edition)

This is a Python-based console game where you guess **who has more Instagram followers** between two randomly selected personalities, brands, or platforms.

---

## 🎮 Gameplay

- You're shown two entities (e.g., Instagram vs Cristiano Ronaldo).
- Each round, you're asked to guess who has **more followers**.
- If you're right, your score increases.
- If you're wrong, the game ends and your final score is shown.

---

## 📂 Project Structure

```bash
📁 higher-lower-game/
├── art.py         # Contains ASCII art logos
├── data.py        # Contains a list of dictionaries with entity data
├── main.py        # Core game logic
├── README.md      # Game documentation
```

---

## 🧠 Example Data Entry (from `data.py`)

```python
{
    'name': 'Instagram',
    'follower_count': 346,
    'description': 'Social media platform',
    'country': 'United States'
}
```

---

## 🧪 How to Run

1. Make sure Python is installed (`>=3.6`).
2. Run the main file:

```bash
python main.py
```

---

## 🛠️ Dependencies

- No external libraries required
- Works cross-platform (Windows, Mac, Linux)

---

## 💡 Features

- Clean CLI interface
- Random selection each round
- ASCII art visuals (from `art.py`)
- Progressive score tracking

---

## 🚧 Future Improvements

- Add difficulty levels
- Include user avatars
- Timer-based challenges
- Save high scores locally

---

## 📸 Sample Output

```
Compare A: Cristiano Ronaldo, Footballer from Portugal
       vs
Compare B: Instagram, Social media platform from United States
You have to choose A or B, Which of these have higher followers on Instagram? a
✅ You win!
Your current score is 1
```

---

## 👨‍💻 Author

Built with Muhammad Rumman Aslam

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

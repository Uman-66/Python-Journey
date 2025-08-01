# 🎨 Turtle Spirograph Art Generator

A mesmerizing visual art generator built with Python's `turtle` graphics! This script creates colorful, circular spirograph patterns using random RGB values.

---

## 🌀 What It Does

- Generates **360-degree circular patterns** (spirographs) using turtle graphics.
- Each circle is drawn at a slightly rotated angle.
- Every pattern is painted in a **random RGB color**, resulting in a vibrant design.

---

## 🖼️ Features

- Uses `turtle.circle()` and `setheading()` for circular motion.
- Dynamic RGB colors via `random.randint()` and `screen.colormode(255)`.
- Fast rendering speed with `timmy.speed("fastest")`.

---

## 🧠 Game Logic

- A loop runs from `0` to `360`, drawing a circle at every degree.
- The turtle’s heading is updated each iteration to rotate the drawing direction.
- Each circle is drawn in a completely **random RGB color**.

---

## 🧾 Project Structure

```bash
📁 turtle-spirograph/
├── main.py          # Main turtle drawing logic
├── colour.py        # (Optional) Predefined colors if needed
├── README.md        # Project documentation
```

---

## 📷 Sample Output

The result is a dazzling circular spirograph, something like a psychedelic flower 🌸 made of 360 colorful loops!

---

## 🛠️ Requirements

- Python 3.6+
- Standard Library only (`turtle`, `random`)
- Optional: `colour.py` for predefined color palettes

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🧪 Function Overview

```python
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
```

---

## 🧹 Possible Enhancements

- Allow user input to control the number of shapes
- Add GUI options (tkinter) for interaction
- Save artwork to file (`canvas.postscript()` or `turtle.getcanvas()`)

---

## 🎨 Extra Ideas

- Try combining it with **Spirograph math formulas**
- Use color gradients for smooth transitions
- Overlay multiple layers with different radii

---

## ✨ Author

Built using `turtle` by a creative monster 🧚‍♂️👹  
Add your name or handle here.

---

## 📜 License

Free to remix and reuse under the MIT License.

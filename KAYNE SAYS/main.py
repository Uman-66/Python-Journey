from tkinter import *
import requests


def get_quote():
    response = requests.get("https://api.kanye.rest/")
    response.raise_for_status()
    data = response.json()
    return data["quote"]


def wrap_text(text, max_width, font):
    words = text.split()
    lines = []
    current_line = []

    for word in words:
        test_line = ' '.join(current_line + [word])
        test_width = len(test_line) * font[1]  # Rough estimation
        if test_width <= max_width:
            current_line.append(word)
        else:
            if current_line:
                lines.append(' '.join(current_line))
            current_line = [word]

    if current_line:
        lines.append(' '.join(current_line))

    return '\n'.join(lines)


def button_click():
    quote = get_quote()
    wrapped_quote = wrap_text(quote, 250, ("Arial", 12))
    canvas.itemconfig(quote_text, text=wrapped_quote)


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)

initial_quote = get_quote()
wrapped_initial_quote = wrap_text(initial_quote, 250, ("Arial", 12))

quote_text = canvas.create_text(
    150,
    207,
    text=wrapped_initial_quote,
    width=250,
    font=("Arial", 16, "bold"),
    fill="white"
)
canvas.grid(row=0, column=0)


kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=button_click)
kanye_button.grid(row=1, column=0)

window.mainloop()
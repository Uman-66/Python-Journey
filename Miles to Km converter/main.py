from tkinter import *
def calculate():
    miles= int(entry.get())
    km = miles * 1.60934.__round__(2)
    Km_label.config(text=km)


window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=400, height=100)
window.config(padx=10, pady=10)

space_label = Label(window, text="                                      ")
space_label.grid(column=0, row=0)



entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(row=0, column=2)

miles_label = Label(window, text="Miles")
miles_label.grid(column=3, row=0)

is_equal_label = Label(window, text="Is Equal to")
is_equal_label.grid(column=0, row=1)

Km_label= Label(window, text="0")
Km_label.grid(column=2, row=1)


km = Label(window, text="Km")
km.grid(column=3, row=1)

button = Button(window, text="Calculate", command=calculate)
button.grid(column=2, row=2)
window.mainloop()

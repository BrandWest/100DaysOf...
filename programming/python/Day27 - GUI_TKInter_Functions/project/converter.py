from tkinter import *

ENTRY = ""
KILOMETERS = ""

def create_gui():
    window = Tk()
    window.title("Mile to KM Converter")
    window.minsize(width=200, height=100)
    kilometers = labeling()
    entry = entry_box()
    button = button_create()

    return window, kilometers, entry, button

def labeling():
    miles = Label(text="Miles")
    miles.grid(column=2, row=0)
    miles.config(padx=10, pady=10)

    equal_to = Label(text="is equal to")
    equal_to.grid(column=0, row=1)
    equal_to.config(padx=10)

    kilometers = Label(text="Km")
    kilometers.grid(column=2, row=1)

    converted = Label(text="0")
    converted.grid(column=1, row=1)

    return converted


def entry_box():
    entry = Entry(width=10)
    entry.insert(END, string="0")
    entry.grid(column=1, row=0)

    return entry


def button_create():
    button = Button(text="Calculate", command=calculate)
    button.grid(column=1, row=2)

    return button


def calculate(**kw):
    kilometer = int(ENTRY.get()) * 1.609344
    kilometer = round(kilometer,1)
    set_label(kilometer, kilometers=KILOMETERS )


def set_label(kilometer, **kw):
    KILOMETERS.config(text=kilometer)


if __name__ == "__main__":
    window, kilometers, entry, button = create_gui()
    ENTRY = entry
    KILOMETERS = kilometers
    window.mainloop()
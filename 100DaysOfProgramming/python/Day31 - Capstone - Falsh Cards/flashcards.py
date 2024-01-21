from tkinter import *
from modules.gui import Gui
from random import randint
import pandas as pd

from modules.cards import Cards

BACKGROUND_COLOR = "#B1DDC6"

def save_progress():
    df = pd.DataFrame.from_dict(card.word_dict)
    df.to_csv('data/words_to_learn.csv', index=False)
    card._saved_progress()


def correct():
    checkmark_button.config(state="disabled")
    window.after_cancel(seconds_remaining)

    del card.word_dict["English"][card.index]
    del card.word_dict["French"][card.index]
    
    save_progress()
    flip_front(seconds_remaining)



def incorrect():
    cross_button.config(state="disabled")
    window.after_cancel(seconds_remaining)
    flip_front(seconds_remaining)


def flip_back():
    window.after_cancel(seconds_remaining)
    print(f"flip_back card index: {card.index}")
    print(f"French {card.word_dict['French'][card.index]}: {card.index}")
    print(f"English {card.word_dict['English'][card.index]}: {card.index}")
    canvas.create_image(0,0, anchor="nw", image=back_image)
    language.config(text="English", bg='#91c2af', fg="white")
    word.config(text=card.word_dict["English"][card.index], bg='#91c2af', fg="white")


def flip_front(seconds_remaining):
    canvas.create_image(0,0, anchor="nw", image=front_image)
    # print(seconds_remaining)
    if seconds_remaining == 3:
        card.random_word()
        print(f"flip_front card index: {card.index}")
        print(f"French {card.word_dict['French'][card.index]}: {card.index}")
        print(f"English {card.word_dict['English'][card.index]}: {card.index}")
        language.config(text="French", bg="white", fg="black")
        word.config(text=card.word_dict["French"][card.index], bg="white", fg="black")
    
    if seconds_remaining > 0:
        cross_button.config(state="disabled")
        checkmark_button.config(state="disabled")
        window.after(3000, flip_front, seconds_remaining - 1)
    elif seconds_remaining == 0:
        cross_button.config(state="normal")
        checkmark_button.config(state="normal")
        flip_back()
    

if __name__ == "__main__":

    root = r"/home/caboose/codingProjects/python/udemy/Day31 - Capstone - Falsh Cards/images/"
    check = root + 'right.png'
    cross = root + 'wrong.png'
    back  = root + 'card_back.png'
    front = root + 'card_front.png'
    seconds_remaining = 3

    card = Cards()
    
    # ============================= WINDOW =============================
    window = Tk()
    window.geometry("900x700")
    window.minsize(width=850 ,height=576)
    window.title("Flashy")
    window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
    
    # ============================= CANVAS =============================
    canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
    back_image = PhotoImage(file=back)
    front_image = PhotoImage(file=front)

    # ============================= CHECK =============================
    checkmark = PhotoImage(file=check)
    checkmark_button = Button(highlightthickness=0, image=checkmark, command=correct, anchor="n")

    # ============================= CROSS =============================
    crossmark = PhotoImage(file=cross)
    cross_button = Button(image=crossmark, highlightthickness=0, command=incorrect, anchor="n")
    
    # ============================= LABELS =============================
    language = Label(font=("Arial",40,"italic"), bg="white")
    # print("first " + str(card.index))
    # card.random_word()
    # print("second " + str(card.index))
    word = Label(font=("Arial", 60, "bold"), bg="white")

    # ============================= PACK =============================
    canvas.grid(column=0, row=0, columnspan=2)
    cross_button.grid(column=0, row=1, sticky="N", pady=10)
    checkmark_button.grid(column=1, row=1, sticky="N", pady=10)
    language.place(x=400, y=150, anchor="n")
    word.place(x=400, y=263, anchor="n")

    flip_front(seconds_remaining)

    
    window.mainloop()
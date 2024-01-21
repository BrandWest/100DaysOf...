import tkinter as tk
BACKGROUND_COLOR = "#B1DDC6"


class Gui(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__()
        root = r"/home/caboose/codingProjects/python/udemy/Day31 - Capstone - Falsh Cards/images/"
        self.check = root + 'right.png'
        self.cross = root + 'wrong.png'
        self.back  = root + 'card_back.png'
        self.front = root + 'card_front.png'
        print(kwargs)
        self.window = kwargs.get("window")
        self.canvas = kwargs.get("canvas")
        self.check_button = kwargs.get("check")
        self.cross_button = kwargs.get("cross")
        
        self.create_gui()
        self.create_canvas()
        self.check_button_func()
        self.cross_button_func()

        self.set_pack()
        self.loop = self.loop()


    def set_pack(self):
        self.canvas.grid(column=0, row=0, columnspan=3)
        self.checkmark_button.grid(column=2, row=2)
        self.cross_button.grid(column=1, row=2)


    def create_gui(self):
        self.window.title("Flashy")
        self.window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)
        self.window.minsize(width=300, height=300)


    
    def create_canvas(self):
        #Canvas
        self.canvas = tk.Canvas(self.window, width=200, height=200)
        self.create_cards


    def check_button_func(self):
        def temp():
            print("temp")
        checkmark = tk.PhotoImage(file=self.check)
        print(f"check: {self.check}\nimage: {checkmark}")
        self.checkmark_button = tk.Button(image=checkmark, command=temp)
        
    
    def cross_button_func(self):
        image = tk.PhotoImage(file=self.cross)
        self.cross_button = tk.Button(self.window, image=image, highlightthickness=0)


    def create_cards(self):
        image = tk.PhotoImage(file=self.front)
        self.canvas.create_image(100, 100, image=image)
        
    def loop(self):
        self.loop = self.window.mainloop()
    

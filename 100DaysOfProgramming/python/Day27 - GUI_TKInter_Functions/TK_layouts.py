from tkinter import *

#Buttons
def button_clicked():
    #changes the name of the label once clicked
    label.config(text=input.get()) #input.get() comes from the input.get() method which returns somethnig


#initalize the window
window = Tk()
window.title("My first gui program")
#Default size 
window.minsize(width=500 ,height=300)
window.config(padx=20, pady=20) #Add pading

'''Things to go into the window'''
#Labels
# label = tkinter.Label(text="I am a label")
label = Label(text="I am a label", font=("Arial", 15))
# label.pack()
# label.place(x=100, y=200)
label.grid(column=0, row=0)
label.config(padx=50, pady=50)

#Configure and change properties of components we've created
# label["text"] = "dictionary Text"
# label.config(text="Will you click me?")


button = Button(text="Click Me!", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

button = Button(text="New Button!", command=button_clicked)
# button.pack()
button.grid(column=2, row=0)

entry = Entry()
entry.grid(column=3, row=2)

'''
LAYOUT MANAGERS

    You can NOT use different layout managers, grid is more flexible and easy to understand.

    Pack: Packs each widgets next to each other Pack will ALWAYS start from the start
        side="Left" # This will move things around
        Complicated
    
    Place: Precicse positioning
        x and y values
        Very specific on wher eto place things

    grid: Make a grid throughout
        Row --->
        Col ^
        Start with the thing from the top left (0, 0)
        then each goes (1,0)
'''
window.mainloop()
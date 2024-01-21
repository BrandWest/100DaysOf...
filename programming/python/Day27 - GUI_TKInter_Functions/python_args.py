'''
    Adv args
        allows a wider range of inputs
        key word args
            function(c=3, a=1, b=2) Keywords let you do it anywhere
        
        Arguments with default values
            def function (a=1, b=2, c=3): #This does not require any inputs.
            
            function()
            or
            function(b=5)
        Adding a custom value vs default value - you can just change the value of b within the function call

        when you have =... within the documents within the import declariation of the function, shows it has dsome defaults
        Any that are optional have defaul values.

        if you want to change the deafult args, you need to do the keyword declarations

        So create functions with default values
'''

import tkinter

#initalize the window
window = tkinter.Tk()
window.title("My first gui program")
#Default size 
window.minsize(width=500 ,height=300)

'''Things to go into the window'''
#Labels
label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
label.pack( side="left", expand=False)


#Keep window on the screen
window.mainloop() #This has to be at the very end of the program.
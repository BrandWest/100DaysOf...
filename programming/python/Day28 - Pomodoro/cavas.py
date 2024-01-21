from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
checks = []

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global checks
    global timer
    global reps

    checks = []

    window.after_cancel(timer)
    timer_label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text=f"0:00")
    pomodoro_label.config(text=checks)
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global checks
    
    reps += 1
    
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Long Break", fg=RED)
        checks += "✔"

    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Short Break", fg=PINK)
        checks += "✔"
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Working", fg=GREEN)
        
        pomodoro_label.config(text=checks)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(seconds_remaining):
    time_remaining_minutes = int(seconds_remaining / 60)
    time_remaining_seconds = int(seconds_remaining % 60)
    
    '''
        Dyanmic Typing
            This is just changing the variables to equal a different type (from int to string)
    '''
    if time_remaining_seconds < 10:
        time_remaining_seconds = f"0{time_remaining_seconds}"
    canvas.itemconfig(timer_text, text=f"{time_remaining_minutes}:{time_remaining_seconds}")
         
    if seconds_remaining > 0:
        global timer
        timer = window.after(1000, count_down, seconds_remaining - 1)
        
    
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="files/tomato.png")
canvas.create_image(100, 112, image=image)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35,"bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer", font=(FONT_NAME, 35), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

pomodoro_label = Label(font=(FONT_NAME, 15), bg=YELLOW, fg=GREEN)
pomodoro_label.config(pady=20)
pomodoro_label.grid(column=1, row=2)


window.mainloop()
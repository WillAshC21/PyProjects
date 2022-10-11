from tkinter import *
import time
from playsound import playsound
from pathlib import Path


#TK inter display window
window = Tk()
window.title("Pomdoro Clock")
window.minsize(width=500, height=500)
window.resizable(False, False)
canvas = Canvas(bg='#FF731D', width=500, height=500)
reset = False




#Pomdoro Clock Title



#Start Button

image = PhotoImage(file="tomato.png")
img_display = canvas.create_image(250, 250, anchor="center", image=image)

work_counter = 0

import random
def countdown(count):
    global  reset
    reset = False
    canvas.delete('time')
    mins, secs = divmod(count, 60)
    clock = '{:02}:{:02}'.format(mins, secs)
    times = canvas.create_text(250, 250, fill="white", text=clock, font=("Arial", 36, "bold"), tags='time')

    if reset == True:
        canvas.delete('time')
        canvas.delete('times')
        times = canvas.create_text(250, 250, fill="white", text=clock, font=("Arial", 36, "bold"), tags='times')

    if count > -1:
        window.after(1000, countdown, count - 1)
    else:
        start_clicked()
    return times

y_pos = 330

#Start function Pomdoro Timer
def start_clicked():
    global work_counter
    global y_pos
    work_counter += 1
    i = 0
    y_pos += 15
    counter = 15
    short_count = 3
    long_count = 9
    audio = Path().cwd() / "alarm.mp3"

    if work_counter %  8 == 0:
        countdown(long_count)
        canvas.destroy('all')
        sound = playsound(audio)

    elif work_counter % 2 == 0:
        countdown(short_count)
        c1 = IntVar()
        c1.set(1)
        checkbox1 = Checkbutton(variable=c1, bg='#FF731D', fg='#38E54D')
        checkbox1.place(x=250, y=y_pos + 5)
        sound = playsound(audio)
    else:
        countdown(counter)
        sound = playsound(audio)

    print(work_counter)




#Reset functionPomdoro Timer
def reset_clicked():
    reset = True
    counter = 1500
    countdown(counter)

button_1 = Button(text="Start", command=start_clicked, font=("Arial", 16, "bold"))
button_1.place(x=120, y=365)

#Reset Button
button_2 = Button(text="Reset", command=reset_clicked, font=("Arial", 16, "bold"))
button_2.place(x=325, y=365)


#Canvas and Window Display
canvas.pack()
window.mainloop()

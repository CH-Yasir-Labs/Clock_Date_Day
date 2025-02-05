#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      chyas
#
# Created:     04/02/2025
# Copyright:   (c) chyas 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
from time import *

is_12_hour_format = False

def update():
    global is_12_hour_format

    if is_12_hour_format:
        time_string = strftime("%I:%M:%S %p")  # 12-hour format with AM/PM
    else:
        time_string = strftime("%H:%M:%S")  # 24-hour format



    time_label.config(text=time_string)

    day_string=strftime("%A")
    day_label.config(text=day_string)

    date_string=strftime("%B %d , %Y")
    date_label.config(text=date_string)

    window.after(1000,update)


def toggle_format():
    global is_12_hour_format
    is_12_hour_format = not is_12_hour_format  # Toggle between True and False
    update()



window = Tk()
window.title("Digital Clock")  # Set title
window.geometry("400x200")  # Set window size
window.resizable(False, False)  # Disable resizing

time_label=Label(window,font=("Arial",50),fg="#00FF00",bg="black")
time_label.pack()

day_label=Label(window,font=("Ink Free",25))
day_label.pack()

date_label=Label(window,font=("Ink Free",30))
date_label.pack()

toggle_button = Button(window, text="Toggle 12/24 Hour", font=("Arial", 15), command=toggle_format, fg="white", bg="black")
toggle_button.pack(pady=10)

update()

window.mainloop()
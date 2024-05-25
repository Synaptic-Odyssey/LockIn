import tkinter
from tkinter import *

url = ""
threshold_value = 0
learning_on = False
lock_in_clicked = False 

def on_change(e):
    global url
    url = e.widget.get()
    # print("Saved value:", url)
    
def on_scale_change(value):
    global threshold_value
    threshold_value = int(value)
    # print("Saved Threshold Value:", threshold_value)
    
def toggle_learning():
    global learning_on
    learning_on = not learning_on
    # print("Learning On:", learning_on)

def lock_in():
    global lock_in_clicked
    lock_in_clicked = True
    # print("Lock In clicked")

window = tkinter.Tk()
window.geometry("450x150")

Label(window, text='Calendar .ics link (hit enter)').grid(row=0)
e1 = Entry(window, width=30, font=('Arial 12'))
e1.grid(row=0, column=1)
e1.bind("<Return>", on_change)

Label(window, text='Select Threshold').grid(row=1)
s1 = Scale(window, from_=0, to=10, length = 200, tickinterval=10, orient=HORIZONTAL, command = on_scale_change)
s1.grid(row=1, column=1)

Button(text="Learning On/Off", width=12, relief="raised", command = toggle_learning).grid(row=2)
Button(text = "Lock In", width=12, relief="raised", command = lock_in).grid(row=2, column=1)

mainloop()



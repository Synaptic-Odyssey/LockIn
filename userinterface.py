import tkinter
from tkinter import *
from LockIn import *
from calendarevent import *
import threading
url = ""
threshold_value = 0
learning_on = False
lock_in_clicked = False 
lock_in_thread=0

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
    t=(threading.Thread(target=learning_start))
    t.start()

def lock_in():
    global lock_in_clicked
    lock_in_clicked = not lock_in_clicked
    global lock_in_thread
    # if  lock_in_thread==0:
        # lock_in_thread=threading.Thread(target=lock_in_start)
        # lock_in_thread.start()
    if lock_in_clicked:
        lock_in_thread=threading.Thread(target=lock_in_start)
        lock_in_thread.start()
def learning_start(): 
    event=get_event("https://calendar.google.com/calendar/ical/1e3a81e23db15db5371aff83435e626e996ef8f26f75b1331ab17ec0efab37ba%40group.calendar.google.com/private-cd3778bb335f55bf428dc4307e5a7994/basic.ics")
  
    while learning_on:
    
        learn(categorize_events(event))
        time.sleep(4)    
def lock_in_start(): 
    event=get_event("https://calendar.google.com/calendar/ical/1e3a81e23db15db5371aff83435e626e996ef8f26f75b1331ab17ec0efab37ba%40group.calendar.google.com/private-cd3778bb335f55bf428dc4307e5a7994/basic.ics")
  
    while lock_in_clicked:
    
        eval_windows(get_category_list(categorize_events(event)),event)
        time.sleep(4)
window = tkinter.Tk()
window.geometry("450x150")

Label(window, text='Calendar .ics link (hit enter)').grid(row=0)
e1 = Entry(window, width=30, font=('Arial 12'))
e1.grid(row=0, column=1)
e1.bind("<Return>", on_change)

Label(window, text='Select Threshold').grid(row=1)
s1 = Scale(window, from_=3, to=10, length = 200, tickinterval=10, orient=HORIZONTAL, command = on_scale_change)
s1.grid(row=1, column=1)

Button(text="Learning On/Off", width=12, relief="raised", command = toggle_learning).grid(row=2)
Button(text = "Lock In", width=12, relief="raised", command = lock_in).grid(row=2, column=1)

mainloop()



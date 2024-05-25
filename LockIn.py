import ollama
from pywinauto import Desktop
from win32gui import FindWindow, PostMessage
import win32.lib.win32con as win32con
from calendarevent import *
def get_current_calander_event():
    return "Coding"
def get_categories():
    return ["Coding","Math","History","Science","Art","Self-Improvement","Exercise", "English"]
def categorize_events(calendar_event):
    categories=get_categories()
    response = ollama.generate(model='llama3', prompt="Which category does the attached calandar event best match? Here are the categories: "+str(categories)+" Here is the calendar event: "+calendar_event+" Please answer with just the name of the category.If the term fits multiple categories respond with both seperated by a comma. Do not add any other words or else")
    return response['response'].replace(" ","").split(",")
def get_category_list(categories):
    # return 
    trainstr="Please respond with the relevance of a window title to the category and current calendar event. Measure relevance on a continuous 0-10 scale with 0 being completly irrelevant and 10 being extremely relevant. I have attached some examples of window title and relevance for the current categories. The current categories are "+ str(categories)+"Examples:"
    for category in categories:
        cat_file=open(".\\Categories\\"+category+".txt", 'r')
        lines=cat_file.readlines()
        for line in lines:
            
            trainstr+=line
    return trainstr
    #Compose a set of strings to train the model on good and bad and then check on the  a lst few and score on a continuous sclae 
def eval_windows(trainstr,calendar_event):
    windows = Desktop(backend="uia").windows()
    for w in windows:
        if(len(w.window_text())>3):    
            print(w.window_text())
            response=ollama.generate(model="llama3", prompt=trainstr+" Please answer just like the examples and take into account the task"+calendar_event+" without any extra text or explaination,just the relevance. Here is the window title: "+w.window_text())
            print(response['response'])
            try:
                
                if(int(response['response'])<=3 and w.window_text()!="Taskbar"):
                    w.minimize()
            except:
                pass
            


def learn(categories):
    windows = Desktop(backend="uia").windows()
    trainstr="Please respond with the relevance of a window title to the category. Take a narrow defemnition of the category. Measure relevance on a continuous 0-10 scale with 0 being completly irrelevant and 10 being extremely relevant. I have attached some examples of window title and relevance for the current categories. The current categories are "+ str(categories)+"Examples:"
    for category in categories:
        cat_file=open(".\\Categories\\"+category+".txt", 'r')
        lines=cat_file.readlines()
        for line in lines:
            trainstr+=line
    print(trainstr)
    for w in windows:
        if(len(w.window_text())>3):    
            print(w.window_text())
            response=ollama.generate(model="llama3", prompt=trainstr+"Please answer without any extra text or explaination, just the relevance. Here is the window title: "+w.window_text())
            try:
                val=int(response['response'])
            except:
                pass
            
            cat_file=open(".\\Categories\\"+categories[0]+".txt", 'a')
            cat_file.write(w.window_text()+","+str(val)+"\n")



# eval_windows(get_category_list(categorize_events("Coding Project"))," Coding Project")
learn(categorize_events(get_event("https://calendar.google.com/calendar/ical/1e3a81e23db15db5371aff83435e626e996ef8f26f75b1331ab17ec0efab37ba%40group.calendar.google.com/private-cd3778bb335f55bf428dc4307e5a7994/basic.ics")))
# def switch_tasks():
#     calandar_event=get_current_calander_event()
#     category=categorize_event(calandar_event)
    #Open categorey and nsdtall internet blocks
    #every 30 seconds if they are focussed on something bad accoridng to the key terms
    #close it
    
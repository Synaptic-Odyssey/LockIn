import ollama
from pywinauto import Desktop
from win32gui import FindWindow, PostMessage
import win32.lib.win32con as win32con
from calendarevent import *
import time
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
    trainstr="Please respond with the relevance of a window title to the category. Take a narrow defenition of the category. Measure relevance on a continuous 0-10 scale with 0 being completly irrelevant and 10 being extremely relevant.Dont give something a score about a 7 if it isnt related to the category I have attached some examples of window title and relevance for the current categories. The current categories are "+ str(categories)+"Examples:"
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
            response=ollama.generate(model="llama3", prompt=trainstr+" Please answer with the relevance and take into account the task"+calendar_event+"  WITHGOU ANY EXTRA TEXT OR EXPLAINATION (or else),just the relevance as a number. Here is the window title: "+w.window_text())
            print(response['response'])
            try:
                
                if(int(response['response'])<=3 and w.window_text()!="Taskbar"):
                    w.close()
            except:
                pass
            


def learn(categories):
    windows = Desktop(backend="uia").windows()
    trainstr="Please respond with the relevance of a window title to the category. Take a narrow defenition of the category. Measure relevance on a continuous 0-10 scale with 0 being completly irrelevant and 10 being extremely relevant.Dont give something a score about a 7 if it isnt related to the category I have attached some examples of window title and relevance for the current categories. The current categories are "+ str(categories)+"Examples:"
    for category in categories:
        cat_file=open(".\\Categories\\"+category+".txt", 'r')
        lines=cat_file.readlines()
        for line in lines:
            trainstr+=line
    # print(trainstr)
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



# learn(categorize_events(event))
# def switch_tasks():
#     calandar_event=get_current_calander_event()
#     category=categorize_event(calandar_event)
    #Open categorey and nsdtall internet blocks
    #every 30 seconds if they are focussed on something bad accoridng to the key terms
    #close it
    
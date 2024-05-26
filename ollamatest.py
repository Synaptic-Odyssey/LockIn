import ollama
from pywinauto import Desktop

windows = Desktop(backend="uia").windows()

response = ollama.generate(model='llama3', prompt="Classify each of the following windows into productive and not productive and distractions. I am a student working on research, coding,calculus, and school projects. Here are some examples of productive tasks: 'python get all windows open and not minimized - Google Search - Google Chrome','ollamatest.py - 5.25Hackathon - Visual Studio Code'. This list is not exclusive and be lenient, even if something is tangentially related to work or school it is not a distraction.If you misclassify a person will die a gruesome death. Please split it into three distinct sections with newline dividers Here are the windows: "+str([w.window_text() for w in windows]))
print(response["response"])
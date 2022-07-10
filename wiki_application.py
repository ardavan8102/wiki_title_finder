# Import Modules
import tkinter as tk
import requests
from bs4 import BeautifulSoup
import webbrowser

# Destination URL
site_url = "https://en.wikipedia.org/wiki/Special:Random"

# Application Main Variables
app = tk.Tk()
app.title("Wiki Title Finder")
app.geometry("700x300")

# Text Bot
text = tk.Text(app, height = 5, width = 32)

# Label
label = tk.Label(app, text = "Read Easily With Me")
label.config( font = ("Courier", 14) )

# Send Request To URL 
def sendRequest(url = site_url):
    text.delete("1.0", tk.END)
    # 2 : Get Data From Site & Inform It To HTML Data
    link = requests.get(url)
    soup = BeautifulSoup(link.content, "html.parser")
    # Convert Title Var To Object (To Use It In Other Function)
    sendRequest.title = soup.find(class_= "firstHeading").text
    # 3 : Convert Heading Data To Text & Put It In Text Bot
    text.insert(tk.END, sendRequest.title)

# Open URL Function
def openUrl():
    t = sendRequest.title
    link = "https://en.wikipedia.org/wiki/%s" %t
    webbrowser.open(link)

# Find Title
findBtn = tk.Button(app, text = "Find", command = sendRequest)

# Open URL
openBtn = tk.Button(app, text = "Open", command = openUrl)

# Quit App
quitBtn = tk.Button(app, text = "Quit", command = lambda:app.quit())

# Packing Elements
text.pack()
label.pack()
findBtn.pack()
openBtn.pack()
quitBtn.pack()

# Insert App Into The Loop
app.mainloop()
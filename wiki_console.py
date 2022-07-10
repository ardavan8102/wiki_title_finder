# Import Modules
import requests
from bs4 import BeautifulSoup
import webbrowser
from colorama import Fore, init
init()

# Infinite Loop (until user breaks it)
while True:

    link = requests.get("https://en.wikipedia.org/wiki/Special:Random") # Send A Request To URL
    soup = BeautifulSoup(link.content, "html.parser") # Transform All Data To HTML Data
    title = soup.find(class_= "firstHeading").text # Convert Heading Data To Text Data

    print("{t}\nOpen The Title?(y/n)\n".format(t = title))

    user_input = input("").lower()

    if user_input == "y": # If Yes :
        link = "https://en.wikipedia.org/wiki/%s" %title # Complete Link Adrress With Putting Site Heading At End of URL
        webbrowser.open(link) # Open The Link With Module
        break

    elif user_input == "n": # If No :
        print(Fore.LIGHTRED_EX + "Current Title Canceled !\n" + Fore.WHITE)
        continue

    else: # If Wrong Input :
        print("Bad Input !")
        break
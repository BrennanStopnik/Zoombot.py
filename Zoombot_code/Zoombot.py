# Modules and Packsges
# Core Python Nods like 
# IF we have buttons on our screen that need to be touched, you have to be leverage another mod called "pyautogui" that we have to int=stall

import schedule
import time
import webbrowser

def open_link(link):
    webbrowser.open(link)

def intro_2_python():
    webbrowser.open("https://dfa.zoom.us/j/96815350328")

def elvis_room():
    webbrowser.open("https://us04web.zoom.us/j/2881787457?pwd=aUZHWlJncS8vL1FoTXlUcWJWaGN4UT09")

schedule.every().monday.at("09:30").do(intro_2_python)
schedule.every().tuesday.at("09:30").do(intro_2_python)
schedule.every().wednesday.at("09:30").do(intro_2_python)
schedule.every().thursday.at("09:30").do(intro_2_python)


while True:
    schedule.run_pending()
    print("Not yet...")
    time.sleep(1)
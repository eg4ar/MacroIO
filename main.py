# Modules
import keyboard
from pyautogui import*
import time
from tkinter import *
import os
import fade
from colorama import Fore

# Modules end

# Variables
enabled = False
macrosio = ("""
  __  __                     _____ ____  
 |  \/  |                   |_   _/ __ \ 
 | \  / | __ _  ___ _ __ ___  | || |  | |
 | |\/| |/ _` |/ __| '__/ _ \ | || |  | |
 | |  | | (_| | (__| | | (_) || || |__| |
 |_|  |_|\__,_|\___|_|  \___/_____\____/ 
                                         
                                         
Press CapsLock to use macro
""")

#os
os.system("title MacroIO by egzre, from https://eg4ar.com/")
faded_text = fade.greenblue(macrosio)
print(faded_text)
print(Fore.RED + "Enabled: False")

def on_caps_lock_press(event):
    global enabled
    enabled = not enabled
    os.system("cls")
    print(faded_text)
    if enabled == False:
        print(Fore.RED + "Enabled:", enabled)
    else:
        print(Fore.GREEN + "Enabled:", enabled)

keyboard.on_press_key('caps lock', on_caps_lock_press)

def spam_io():
    while enabled:
        keyboard.press("i")
        time.sleep(0.01)
        keyboard.release("i")
        time.sleep(0.01)
        keyboard.press("o")
        time.sleep(0.01)
        keyboard.release("o")
        time.sleep(0.01)
        keyboard.press("i")
        time.sleep(0.01)
        keyboard.release("i")
        time.sleep(0.01)
        keyboard.press("o")
        time.sleep(0.01)
        keyboard.release("o")
        time.sleep(0.01)
# Main loop
if __name__ == '__main__':
    while True:
        spam_io()
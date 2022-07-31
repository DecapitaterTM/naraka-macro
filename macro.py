import keyboard
import time
import fade
from colorama import Fore, Back, Style
import os
import random

fade_me = """
  _   _                 _         ____  _           _                  _       _     __  __                      
 | \ | |               | |       |  _ \| |         | |                (_)     | |   |  \/  |                     
 |  \| | __ _ _ __ __ _| | ____ _| |_) | | __ _  __| | ___ _ __   ___  _ _ __ | |_  | \  / | __ _  ___ _ __ ___  
 | . ` |/ _` | '__/ _` | |/ / _` |  _ <| |/ _` |/ _` |/ _ \ '_ \ / _ \| | '_ \| __| | |\/| |/ _` |/ __| '__/ _ \ 
 | |\  | (_| | | | (_| |   < (_| | |_) | | (_| | (_| |  __/ |_) | (_) | | | | | |_  | |  | | (_| | (__| | | (_) |
 |_| \_|\__,_|_|  \__,_|_|\_\__,_|____/|_|\__,_|\__,_|\___| .__/ \___/|_|_| |_|\__| |_|  |_|\__,_|\___|_|  \___/ 
                                                          | |                                                    
                                                          |_|                                                    """
fade_me2 = """
     __                _           ___ _           _                  _       _                                 
  /\ \ \__ _ _ __ __ _| | ____ _  / __\ | __ _  __| | ___ _ __   ___ (_)_ __ | |_    /\/\   __ _  ___ _ __ ___  
 /  \/ / _` | '__/ _` | |/ / _` |/__\// |/ _` |/ _` |/ _ \ '_ \ / _ \| | '_ \| __|  /    \ / _` |/ __| '__/ _ \ 
/ /\  / (_| | | | (_| |   < (_| / \/  \ | (_| | (_| |  __/ |_) | (_) | | | | | |_  / /\/\ \ (_| | (__| | | (_) |
\_\ \/ \__,_|_|  \__,_|_|\_\__,_\_____/_|\__,_|\__,_|\___| .__/ \___/|_|_| |_|\__| \/    \/\__,_|\___|_|  \___/ 
                                                         |_|                                                    """

print("please note slidehop isnt finished")
legit_or_not  = input("Do you want to use the preset legit macro? \n [Y/N or Z for slidehop]")
inputkey = input("input the key to toggle the macro or slidehop \n")
keyspamkey = input("input your binded escape key. Default key is 'e' \n")
time_delay = float(input("[IGNORE IF YOU ARE USING THE LEGIT MODE] \nplease input your time delay. Note: 0.09 is recommended to avoid a ban \n"))
funwalk = input("input the key to toggle the funnywalk")
#tap_dodge_key = input("input the key to toggle Tap Dodge")
tap_dodge_key = "w"

fade_text = fade.purplepink(fade_me)
fade_text2 = fade.purplepink(fade_me2)

#to clear the text for inputting stuff
os.system('cls')
print(Style.RESET_ALL)

#code to make naraka autolaunch without ac
#got lazy will prob remain unfinished
#"C:\Program Files (x86)\Steam\steamapps\common\NARAKA BLADEPOINT\NarakaBladepoint.exe" "naraka&#@$$(%#$"
#os.system("cmd")
#print(Fore.MAGENTA + "your game will autolaunch without the anticheat shortly")
#time.sleep(10)


#while loop to spam key
def not_legit_loop():
    while keyboard.is_pressed(inputkey):
        keyboard.press(keyspamkey)
        keyboard.release(keyspamkey)
        time.sleep(time_delay)
        
    else:
        time.sleep(0.01)

def legit_loop():
    while keyboard.is_pressed(inputkey):
        randomflt = random.uniform(0.01, 0.05)
        randomflt2 = random.uniform(0.01, 0.05)
        keyboard.press(keyspamkey)
        time.sleep(randomflt)
        keyboard.release(keyspamkey)
        time.sleep(randomflt2)
    else:
        time.sleep(0.01)

def slidehop():
    while keyboard.is_pressed(inputkey):
        keyboard.press("c")
        time.sleep(1)
        keyboard.release("c")
        keyboard.press("space")
        keyboard.release(0.25)

def funny_walk():
    while keyboard.is_pressed(funwalk):
        keyboard.press("w")
        time.sleep(0.05)
        keyboard.release("w")
        time.sleep(0.1)
    else:
        time.sleep(1)

def tap_dodge():
    while keyboard.is_pressed(tap_dodge_key):
        keyboard.press("s")
        keyboard.press("left shift")
        keyboard.release("s")
        keyboard.release("left shift")
        time.sleep(0.7)
        keyboard.press("s")
        keyboard.press("left shift")
        keyboard.release("s")
        keyboard.release("left shift")
    else:
        time.sleep(0.05)


if legit_or_not.upper().startswith("Y") == True:
    fade_text = fade.purplepink(fade_me)
    print(fade_text)
    print(Fore.MAGENTA + "                                                                                            Made by: courted")
    print('Your current toggle key is "' + inputkey + '" and your current key to spam is "' + keyspamkey + '"')
    while True:
        legit_loop()
        funny_walk()
#        tap_dodge()

elif legit_or_not.upper().startswith("Z") == True:
    fade_text = fade.purplepink(fade_me)
    print(fade_text)
    print(Fore.MAGENTA + "                                                                                            Made by: courted")
    print('slidehop key is "' + inputkey + '"')
    while True:
        legit_loop()
        funny_walk()

else:
    print(fade_text2)
    print(Fore.MAGENTA + "                                                                                            Made by: courted")
    print('Your current toggle key is "' + inputkey + '" and your current key to spam is "' + keyspamkey + '"')
    print('the time delay on spam is "' + str(time_delay) + '"')
    print("Note: the 0.09s time delay will average 45-55 key presses")
    while True:
        not_legit_loop()
        funny_walk()



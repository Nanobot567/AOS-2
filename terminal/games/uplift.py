from yaspin import yaspin
from yaspin.yaspin.spinners import Spinners
from time import sleep
from random import randint
phase = 0
action = ""
username = ""
seed = 0
room = "null"
inventory = ["pencil"]
achievements = []

# UPLIFT created on 4/6/2020

print("\n")
with yaspin.yaspin(Spinners.material, text="") as sp:
    sleep(2)



print("""

      ___           ___                                   ___               
     /__/\         /  /\                    ___          /  /\        ___   
     \  \:\       /  /::\                  /  /\        /  /:/_      /  /\  
      \  \:\     /  /:/\:\  ___     ___   /  /:/       /  /:/ /\    /  /:/  
  ___  \  \:\   /  /:/~/:/ /__/\   /  /\ /__/::\      /  /:/ /:/   /  /:/   
 /__/\  \__\:\ /__/:/ /:/  \  \:\ /  /:/ \__\/\:\__  /__/:/ /:/   /  /::\   
 \  \:\ /  /:/ \  \:\/:/    \  \:\  /:/     \  \:\/\ \  \:\/:/   /__/:/\:\  
  \  \:\  /:/   \  \::/      \  \:\/:/       \__\::/  \  \::/    \__\/  \:\ 
   \  \:\/:/     \  \:\       \  \::/        /__/:/    \  \:\         \  \:|
    \  \::/       \  \:\       \__\/         \__\/      \  \:\         \__\/
     \__\/         \__\/                                 \__\/              


                              an adventure game
                                by NANOBOT567


""")
input("                           Press [ENTER] to start.")

seed = randint(1, 100)
sleep(1)
print("Seed: \n")
print(seed)
sleep(1)
username = input("What is your name? ")
if username == "Aiden":
    sleep(3)
    print("\nYou are about to meet someone")
    sleep(2)
    print("\nvery")
    sleep(1)
    print("\nvery")
    sleep(1)
    print("\ninteresting, Aiden.")
sleep(4)
print("\n" * 80)

with yaspin.yaspin(Spinners.material, text="") as sp:
    sleep(3)
sleep(0.8)

print("\n" * 80)

sleep(2)

print("MARCH 6, 2069")
sleep(1)
print("\n")
sleep(0.3)
print("\n")
sleep(1)
print("You hear a crash from someplace in your house.")
print("(type help for help with UPLIFT.)")
room = "bedroom"
while action != "esc":
    action = input("UPLIFT: ")
    if action == "help":
        print("commands: goto, look, look harder, check [item], pickup [item], throw away [item in inventory], attack [entity]")
        print("in battle: eat [food item], hit with [weapon], shoot with [gun], throw [item], achievements")
    elif action == "achievements":
        print("\nHere are the achivements you've gotten this session:\n")
        print(achievements)
    elif action == "goto":
        action = input("Position: ")
        if action == "parents room":
            if room == "bedroom" or "kitchen" or "bathroom" or "living room":
                print("You walked into your parents' room.")
                room = "parents' room"
        if action == "bedroom":
            if room == "bedroom" or "kitchen" or "bathroom" or "living room":
                print("You walked into your room.")
                room = "bedroom"
    elif action == "look":
        if room == "bedroom":
            print("You see your bed, a note, a vr headset, a computer, a desk, and a closet.")
            print("In your house, there are 5 rooms: your bedroom, your parents room, the bathroom, the kitchen, and the living room.")
        elif room == "parents' room":
            print("It's your parents room. There's a bed and two nightstands next to it and a Dell windows 10 computer.")
    elif action == "check":
        action = input("Check what? ")
        if room == "bedroom":
            if phase == 1:
                if action == "person" or "kid" or "kid with jetpack":
                    action = input("What would you like to say? [1: Who are you? 2: Where'd you get the jetpack? 3: Get the f*** out of my house!] ")
                    if action == "1":
                        print('\n"My name is 982.", he says. "We dont have much time,', username,'." They will be here soon.\n')
                        action = input("[1: Who's they? 2: How'd you know my name? 3: How do I know you're not messing with me?] ")
                    elif action == "2":
                        print('\nHe shrugs. "Classified."')
                        sleep(1)
                        print('"Anyways, they are coming. Grab a weapon. Anything."')
                        action = input("[1: Why should I? 2: I don't think I have anything... 3: ...")
                    elif action == "3":
                        print('\n"I guess you wanna die then. See ya." He fires up his jetpack and busts through the roof.')
                        sleep(2)
                        print("You don't notice a strange object on the outside part of the window. It beeps. And beeps again.")
                        sleep(3)
                        print("It keeps on beeping! Faster and faster! You just lay in your bed thinking he was a weirdo!")
                        sleep(3)
                        print("THE BEEPING SOUND FROM THE OBJECT GOES SO FAST THA- Oh, wait. Are you dead now? Dang.")
                        sleep(3)
                        print("\n")
                        sleep(0.8)
                        print("\n")
                        sleep(0.8)
                        print("You died from a fiery explosion! Achievement unlocked: You are such an idiot.")
                        achievements.append("You are such an idiot.")
                        sleep(2)
                        action = input("Would you like to try again? [Y/N] ")
                        if action == "Y" or "y":
                            with yaspin.yaspin(Spinners.material, text="Restarting...") as sp:
                                sleep(3)
                        elif action == "N" or "n":
                            with yaspin.yaspin(Spinners.material, text="Shutting down UPLIFT...") as sp:
                                sleep(2)
                            quit()
                else:
                    print("I don't understand that.")
            elif phase == 0:
                
                    
                if action == "note":
                    print("It's a note from your mom and dad.")
                    print("\nIt says: Hi, "+ username + "! We went to the store to grab literally everything, so hang in there!")
                elif action == "headset" or "vr headset":
                    print("Your VR headset. Last time you played it, you were playing SUPERHOT. You're pretty much a part of the hackers already.")
                    action = input("Put it on? [Y/N] ")
                    if action == "Y" or "y":
                        print("You put on the headset, and the light inside shows another room with lots of screens and a disk. \n")
                        sleep(1)
                        print("You put the disk in the drive.\n")
                        sleep(2)
                        print("You play for hours.\n")
                        sleep(5)
                        print("You feel a tap on your back right as you finish a level.\n")
                        sleep(1)
                        print("It's a kid, with a jetpack. He looks almost exactly like you.\n")
                        phase = 1

                    elif action == "N" or "n":
                        print("You put the headset back on the desk.")
            elif room == "parents' room":
                if action == "computer":
                    print("\nYou open the laptop to find that it's dead. Wonderful, right?\n")
                else:
                    print("I don't understand that.")
            

    print("\n")
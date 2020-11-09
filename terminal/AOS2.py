# AOS version 2
# Started working on it on April 3, 2020

from modules.yaspin import yaspin
from modules.yaspin.yaspin.spinners import Spinners

from modules import progressbar

import time

import sys

import os

pword = ""

cmd = ""

directory = ""

ays = ""

net = ""

i = 0



DOSbatDwnld = "no"

succBatDwnld = "no"

crashProgram = "[NOT_DEFINED]"

# crash handler is loaded first, in case the startup fails.
def crash(crashProgram):
    time.sleep(1)
    print("\n" *50)
    print("\u001b[31mAOS has sent the following message: \n")
    print("Your computer has been shut down because of the program \u001b[44m\u001b[1m[" + crashProgram + "]\u001b[0m\n \u001b[31mPlease restart your computer, and enter recovery mode by pressing [R] on startup to retrieve your files. \n")
    print("If this keeps happening, please contact your PC provider.")
    time.sleep(8)
    print("\n"*3)
    shutdown()

def shutdown():
    print("\u001b[31m\nshutting down AOS...\u001b[0m")
    time.sleep(2)
    exit()

# ...never worked anyway.
def notes():
    print("Welcome to notes! type 'nhelp' for help with notes.")
    cmd = ""
    while cmd != "esc":
        cmd = input("\nAOST/notes/: ")
        if cmd == "nhelp":
            print("availible commands:")
            print("new ", "close ", "edit ", "delete \n")
            while cmd != "esc":
                cmd = input("\nAOST/notes/help/: ")
                if cmd == "new":
                    print("the new command allows you to create a new text file.")
                if cmd == "close":
                    print("the close command closes the current document.")
                if cmd == "edit":
                    print("the edit command edits a document.")
                if cmd == "delete":
                    print("the delete command deletes a document.")
                if cmd == "new":                        
                    cmd = input("Please type the name of the new file: ")
                    filename = cmd 
                    cmd = input("Please select the filetype: ")
                    filetype = cmd
                    f = open(filename + "." + filetype, "w")
                    cmd = input("Now type what is in the file: ")
                    f.write(cmd)
                    print("done.")
                    f.close

# here we go. this is going to take a heck of a long time.
def config():
    cmd = ""
    print("configure your AOS terminal. type help for help with config, quit to quit.")
    while cmd != "quit":
        cmd = input("config$ ")
        if cmd == "help":
            print("showing all config$ commands.")
        if cmd == "terminate":
            print("DELETES ALL AOS FILES FROM COMPUTER.")

    with yaspin.yaspin(Spinners.line, text="exiting config mash and saving changes...") as sp:
        time.sleep(2)
    print("\n\n")
    time.sleep(1)
    startup()

# just the help section. needed to seperate this from everything bc of OrGaNiZaTiOn
def help():
    cmd = "null"
    print("\nshowing all availible commands. ")
    print("help","fl","dir ", "esc ", "quit ", "gamePortal ", "notes ", "clock ", "calculator ", "install ", "kBrowse ", "shutdown ", "configure \n")
    print("showing all availible filetypes. ")
    print("x", " txt ", "rndr ", "ps ", "kbpp ", "arg ", "bat \n")
    print("type 'help' for the list again.")
    while cmd != "esc":
        cmd = input("\nAOST/help/: ")
        if cmd == "dir":
            print("dir is used in fl to show everything in the directory.")
            print("for example: \n \n")
            print("AOST: fl")
            print("AOST/fl: dir")
            print("junk.rndr morejunk.txt main.x")
            print("\ndir can also be used with the extension -h to view hidden files as well as regular files.")
        if cmd == "fl":
            print("fl is the standard file launcher for AOS, and can open any supported filetype.")
            print("for example: \n \n")
            print("AOST/: fl")
            print("AOST/fl: readme.txt")
            print("\n thanks for reading me :D")
        if cmd == "esc":
            print("esc allows you to quit any program that is running. can be used within anything, even this. so, you should probably open help again if you would like to keep searching.")
        if cmd == "shutdown":
            print("can only be used in the directory AOST. quits AOS.")
        if cmd == "help":
            print("\nshowing all availible commands. ")
            print("help","fl","dir ", "esc ", "quit ", "gamePortal ", "notes ", "clock ", "calculator ", "install ", "kBrowse \n")
            print("showing all availible filetypes. ")
            print("x", " txt ", "rndr ", "ps ", "kbpp ", "arg ", "bat \n")
        if cmd == "gamePortal":
            print("gamePortal is a built-in game engine that can run any installed game.")
        if cmd == "clock":
            print("clock is a program that lets you see the time and date in your area.")
        if cmd == "calculator":
            print("Calculator is an app that can do simple equasions.")
        if cmd == "kBrowse":
            print("kBrowse is a simple web browser using the ethernet service pdModem.")
        if cmd == "install":
            print("install lets you download certain files from the internet.")
        if cmd == "configure":
            print("configure can be used (as of now) only in the AOST root. It sends you to the configOS, to configure your AOS system.")
        if cmd == "x":
            print(".x is a cross-platform filetype that can be read in MacOS as well as in AOS.")
        if cmd == "txt":
            print(".txt is a standard, formatted text filetype.")
        if cmd == "rndr":
            print(".rndr is a renderable file, meaning it can be used to run simple programs in potatoScript, KBall++, and more.")
        if cmd == "ps":
            print(".ps is the potatoScript filetype, and can be read by a potatoScript reader like smilePotato.")
        if cmd == "kbpp":
            print(".kbpp is the Kball++ filetype, and can be read by a KBPP debugger or runner such as SamolCamel Reader.")
        if cmd == "arg":
            print(".arg is the AOS renderable game filetype. it is used in AOS gamePortal as it is made for a game engine.")
        if cmd == "dev/load":
            i = 0
            for i in progressbar.pb(range(20), "testing pb... ", 30):
                time.sleep(0.1)
            with yaspin.yaspin(Spinners.line, text="testing yaspin...") as sp:
                time.sleep(2)
        if cmd == "dev/sound":
            pass




# scr!
def samol():
    with yaspin.yaspin(Spinners.line, text="Starting [SCR]...") as sp:
        time.sleep(2)
    time.sleep(2)
    print("""

                             _______  _______  __   __  _______  ___        _______  _______  __   __  _______  ___       
                            |       ||   _   ||  |_|  ||       ||   |      |       ||   _   ||  |_|  ||       ||   |      
                            |  _____||  |_|  ||       ||   _   ||   |      |       ||  |_|  ||       ||    ___||   |      
                            | |_____ |       ||       ||  | |  ||   |      |       ||       ||       ||   |___ |   |      
                            |_____  ||       ||       ||  |_|  ||   |___   |      _||       ||       ||    ___||   |___   
                             _____| ||   _   || ||_|| ||       ||       |  |     |_ |   _   || ||_|| ||   |___ |       |  
                            |_______||__| |__||_|   |_||_______||_______|  |_______||__| |__||_|   |_||_______||_______|  
                                             ______    _______  _______  ______   _______  ______                         
                                            |    _ |  |       ||   _   ||      | |       ||    _ |                        
                                            |   | ||  |    ___||  |_|  ||  _    ||    ___||   | ||                        
                                            |   |_||_ |   |___ |       || | |   ||   |___ |   |_||_                       
                                            |    __  ||    ___||       || |_|   ||    ___||    __  |                      
                                            |   |  | ||   |___ |   _   ||       ||   |___ |   |  | |                      
                                            |___|  |_||_______||__| |__||______| |_______||___|  |_|   


                                                                the kbpp reader
    
    """)
    print("As of now, SCR can only read pre-set kbpp files.")
    print("\nif you are having trouble with SCR, please type scrhelp.")
    cmd = ""
    while cmd != "esc":
        cmd = input("AOST/SCR/: ")
        if cmd == "scrhelp":
            print("showing all availible commands...")
            print("\nrun ", "debug ", "render ", "shell \n")
            print("showing all availible kbpp files...")
            print("\ndialogtest.kbpp ", "username.kbpp \n")
            while cmd != "esc":
                cmd = input("AOST/SCR/help/: ")
                if cmd == "run":
                    print("Run allows you to run a kbpp document. syntax: run test")
                if cmd == "debug":
                    print("debug lets you debug a kbpp file. It will output 'no errors' if it is fine, or an error will pop up.")
                if cmd == "render":
                    print("render makes a kbpp file into a renderable doc.")
                if cmd == "shell":
                    print("shell is the K-Ball++ shell prompt.")
        if cmd == "run":
            while cmd != "esc":
                print("Please select the kbpp file to run.\n")
                cmd = input("AOST/SCR/run/: ")
                if cmd == "dialogtest":
                    pass
                if cmd == "username":
                    from getpass import getuser
                    un = getuser()
                    print("the main username is " + un)
        if cmd == "debug":
            while cmd != "esc":
                print("Please select the kbpp file to debug.\n")
                cmd = input("AOST/SCR/debug/: ")
                if cmd == "dialogtest":
                    with yaspin.yaspin(Spinners.line, text="Starting [SCR]...") as sp:
                        time.sleep(0.3)
                    print("no errors.\n\n")
                if cmd == "username":
                    with yaspin.yaspin(Spinners.line, text="Starting [SCR]...") as sp:
                        time.sleep(0.3)
                    print("no errors.\n\n")
        if cmd == "shell":
            pass



# very shaky gamePortal.
def gamePortal():
    cmd = ""
    print("GAMEPORTAL \n \n")
    time.sleep(1)
    print("the game engine of the future(TM) \n \n")
    time.sleep(1)
    print("Welcome to gamePortal! This is a pre-installed game engine that can play any installed game. To install a game, type install and the game you want to install. Please note that to cons- \n")
    print("erve space on your AOS system, the games will uninstall after they have been used. (type gpHelp for help and games that you can install.)")
    while cmd != "esc":
        cmd = input("AOST/gp/: ")
        if cmd == "gpHelp":
            print("list of commands in gp:")
            print("install", " esc", "\n")
            print("list of games you can download:")
            print("sample.arg ", "droids.arg \n")
            while cmd != "esc":
                cmd = input("AOST/gp/help/: ")
                if cmd == "install":
                    print("the install command is used for installing a game. syntax: install sample.arg")
                    if cmd == "esc":
                        print("esc is used for quitting either gamePortal or help, which you just did for help.")
        if cmd == "install sample":
            i = "dummy"
            for i in progressbar.pb(range(20), "installing 'sample.arg': ", 20):
                time.sleep(0.05)         
            print("done! running 'sample.arg'...")
            time.sleep(0.8)
            cmd = input("great job, you ran me! type 'esc' to exit... ")
            while cmd != "esc":
                cmd = input("great job, you ran me! type 'esc' to exit... ")
        if cmd == "install droids":
            print("\n" *4)
            for i in progressbar.pb(range(30), "checking if 'droids.py' is present... ", 15):
                time.sleep(0.01)
            print("\n")
            for i in progressbar.pb(range(10), "checking for modules in 'droids.py'... ", 10):
                time.sleep(0.02)
            print("\n")
            for i in progressbar.pb(range(100), "downloading code in 'droids.py'... ", 10):
                time.sleep(0.06)
            print("\n")
            print("Done! Running...")
            time.sleep(1)
            if cmd == "install droids":
                cmd = input("WARNING this will quit AOS. The game will reboot AOS after the script is finished. Are you OK with this? [Y/N] ")
                if cmd == "Y" or "y":
                    print("type 'help' for help with droids.py.")
                    os.system('python /Users/Nanobot567/Desktop/AOS/terminal/games/droids.py')
                    quit()
                
            else:
                print("ERROR while parsing droids.py, quitting.")



# need to set this straight. how the heck do you make a string into an integer?!!??!
# duh. transform it into an int using int.
def calc():
    #from apps import calc
    crash("[CALCULATOR.RNDR]")

        

                    
                

# kBrowse browser attribute.
def kBrowse():
    with yaspin.yaspin(Spinners.line, text="Opening KBROWSE...") as sp:
        time.sleep(1)
    print("""
    
                                        ██╗  ██╗██████╗ ██████╗  ██████╗ ██╗    ██╗███████╗███████╗
                                        ██║ ██╔╝██╔══██╗██╔══██╗██╔═══██╗██║    ██║██╔════╝██╔════╝
                                        █████╔╝ ██████╔╝██████╔╝██║   ██║██║ █╗ ██║███████╗█████╗  
                                        ██╔═██╗ ██╔══██╗██╔══██╗██║   ██║██║███╗██║╚════██║██╔══╝  
                                        ██║  ██╗██████╔╝██║  ██║╚██████╔╝╚███╔███╔╝███████║███████╗
                                        ╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚═════╝  ╚══╝╚══╝ ╚══════╝╚══════╝
    
                                            browse the RiptideNet in the fastest way possible
    

    """)

    print("This is KBROWSE, brought to you by kBall Industries.")
    print("\nType 'khelp' for help with kBrowse.\n")
    cmd = ""
    net = "no"
    while cmd != "esc":
        cmd = input("AOST/kBrowse/: ")
        if cmd == "khelp":
            print("showing all availible commands...")
            print("search ", "connect ", "disconnect ", "esc \n")
            print("showing all availible websites...")
            print("kBall.com ", "com.com ", "riptideimages.com")
            while cmd != "esc":
                cmd = input("AOST/kBrowse/khelp/: ")
                if cmd == "search":
                    print("you use the command search to open the search bar.")
                if cmd == "connect":
                    print("connect connects you to the internet, if you have your pdModem thumbdrive inserted. If you need help with connecting your pdModem, type pdHelp.")
                if cmd == "disconnect":
                    print("the disconnect command disconnects you from the current network.")
                if cmd == "netConnect -pdM +wifi":
                    print("first off, how did you find this command? anyway.. this connects you to the network without using a pdModem thumbdrive.")
        if cmd == "connect":
            pass
            # note to self: make sure this checks that the drive is inserted and "connects" accordingly. dunno how this will work.
        if cmd == "netConnect -pdM +wifi":
            net = "yes"
            print("successfully connected.")
        if cmd == "search":
            if net == "yes":
                print("-------------------------------------------------------------------------")
                while cmd != "esc":
                    cmd = input("AOST/kBrowse/search/: ")
                    if cmd == "kBall.com":
                        print("kBall.com is currently in development. we're sorry for the inconveinence.")
                        # from websites import kball.py
                    if cmd == "com.com":
                        from websites import com
                    if cmd == "riptideimages.com":
                        pass
            else:       
                print("sorry, but you're not connected to the internet. please check your connection and try again.")



# startup is kind of the full engine for AOS. 
def startup():
    cmd = "null"
    print("starting up AOS  \n")
    time.sleep(0.6)
    print("\u001b[7mif you need help with AOS, please type help into the command prompt. \u001b[0m\n")
    time.sleep(1)
    while cmd != "shutdown":
        cmd = input("\nAOST/: ")
        directory = "main"
        if cmd == "help":
            help()
        if cmd == "fl":
            while cmd != "esc":
                cmd = input("AOST/fl/: ")
                if cmd == "dir":
                    if directory == "main":
                        print("pypoem.txt", " fl.rndr", "virus.rndr", " money.rndr ", "SamolCamelReader.rndr ")
                if cmd == "dir -h":
                    if directory == "main":
                        print("pypoem.txt", " fl.rndr", " virus.rndr", " money.rndr", "SamolCamelReader.rndr " " .superhot")
                if cmd == "pypoem.txt":
                    import this
                    print("\n" *3)
                if cmd == "virus.rndr":
                    print("Ha! You just activated a virus! Have fun restarting!")
                    time.sleep(1)
                    print("LOL" *1000)
                    crash("[NULL]")
                if cmd == "money.rndr":
                    print("""
                    
                    $$$$$$$$  $$$$$  $$$$  $$$$  $   $  $$
                    $$  $  $  $$  $  $  $  $$$$  $   $  $$
                    $$  $  $  $$  $  $  $  $     $$$$$  
                    $$  $  $  $$$$$  $  $  $$$$    $    $$

                     """)
                if cmd == ".superhot":
                    print("\033[1;31;40m\n")
                    print("GO INTO FULLSCREEN.")
                    time.sleep(1)
                    while "1" == "1":
                        print("""    
                                                             _____ _____ _____ _____ _____   
                                                            |   __|  |  |  _  |   __| __  |  
                                                            |__   |  |  |   __|   __|    -|  
                                                            |_____|_____|__|  |_____|__|__|  

                                 """)
                        time.sleep(1)
                        print("""
                                                                   _____ _____ _____ 
                                                                  |  |  |     |_   _|
                                                                  |     |  |  | | |  
                                                                  |__|__|_____| |_|
                    
                        """)
                        time.sleep(1)
                if cmd == "SamolCamelReader.rndr":
                    samol()
        if cmd == "kBrowse":
            kBrowse()
        if cmd == "gamePortal":
            print("opening gameportal... \n \n")
            gamePortal()
        if cmd == "notes":
            print("Notes is soon to be implemented into AOS. We're sorry for the inconvienience this could have caused.")
        if cmd == "clock":
            print("Welcome to clock, the best way to view time(TM).")
            time.sleep(1)
            print("If you need help with clock, please type chelp.")
            while cmd != "esc":
                cmd = input("AOST/clock: ")
                if cmd == "chelp":
                    print("showing all commands...")
                    print("\n time ", "date ", "\n")
                    while cmd != "esc":
                        cmd = input("AOST/clock/help: ")
                        if cmd == "time":
                            print("the 'time' command lets you view the current time in your area. \n")
                        if cmd == "date":
                            print("the 'date' command lets you see the current month, day, and year, in that order.")
                if cmd == "time":
                    print(time.strftime('\n%X %Z\n'))
                if cmd == "date":
                    print(time.strftime('\n%x %Z \n'))
        if cmd == "calculator":
            calc()
        if cmd == "install":
            while cmd != "esc":
                cmd = input("AOST/install/: ")
                if cmd == "help":
                    print("This is the install command prompt, where you can download anything that is availible. Type help/a for the list of things you can download. (When you want to download a file, make sure you add the filetype at the end)")
                if cmd == "help/a":
                    print("Installable files: DOS.bat SUCC.kbpp")
                if cmd == "SUCC.kbpp":
                    cmd = input("Are you sure you want to download this file? [Y/N] ")
                    if cmd == "Y" or "y":
                        succBatDwnld = "yes"
                        for i in progressbar.pb(range(100), "downloading main assets for [SUCC.kbpp]... ", 10):
                            time.sleep(0.01)
                        for i in progressbar.pb(range(100), "scanning for viruses... ", 10):
                            time.sleep(0.03)
                        for i in progressbar.pb(range(100), "sending to [SCR]... ", 10):
                            time.sleep(0.05)
                        for i in progressbar.pb(range(100), "cleaning up... ", 10):
                            time.sleep(0.001)
                        print("Done!")
                        time.sleep(0.6)
                        print("To run your downloaded file, go into SCR and type in the filename.")
                        print("WARNING: PLEASE CHECK YOUR CONFIG FILE. YOU MIGHT HAVE THE 'DELETE ON REBOOT' SET ON 1, IN DOWNLOADS.")
                if cmd == "DOS.bat":
                    cmd = input("Are you sure you want to download this file? [Y/N] ")
                    if cmd == "Y" or "y":
                        DOSbatDwnld = "yes"
                        for i in progressbar.pb(range(100), "downloading assets for [DOS.bat]... ", 10):
                            f = open("downloads.aos", "r+")
                            if succBatDwnld == "yes":
                                readTxt = "succ.kbpp\n"
                            f.write(readTxt+"DOS.bat")
                            f.close
                        for i in progressbar.pb(range(100), "checking for batRead.rndr... ", 10):
                            time.sleep(0.01)
                        for i in progressbar.pb(range(100), "scanning for viruses... ", 10):
                            time.sleep(0.03)
                        for i in progressbar.pb(range(100), "converting to .rndr... ", 10):
                            time.sleep(0.05)
                        for i in progressbar.pb(range(100), "cleaning up... ", 10):
                            time.sleep(0.001)
                        print("Done!")
                        time.sleep(0.6)
                        print("To run your downloaded file, go into fl and type in the filename. You may have to change directories, and to do that use cd and the directory.")
                        print("WARNING: PLEASE CHECK YOUR CONFIG FILE. YOU MIGHT HAVE THE 'DELETE ON REBOOT' SET ON 1, IN DOWNLOADS.")
                    if cmd == "N" or "n":
                        pass
        if cmd == "configure":
            config()

# AOS Startup msgs
print("\033[1;37;40m \u001b[0m \n")
with yaspin.yaspin(Spinners.line, text="Starting up [MAIN.OS]...") as sp:
    time.sleep(1)
    sp.write("\n\u001b[32mSuccesfully started [MAIN.OS]  \u001b[0m\n")

with yaspin.yaspin(Spinners.line, text="Checking for modules...") as sp:
    time.sleep(0.7)
    sp.write("\n\u001b[32mModules detected  \u001b[0m\n")


with yaspin.yaspin(Spinners.line, text="Looking for [filecmdr.rndr]") as sp:
    time.sleep(0.1)
    sp.write("\n\u001b[32m[filecmdr.rndr] present. Beginning boot.  \u001b[0m\n")

# rndr is short for render. i wanted to make something else other than .exe or .app, so i did that.
with yaspin.yaspin(Spinners.line) as sp:
    time.sleep(2)
if pword == "":
    startup()    


    # this may seem random, but it's the shutdown command prompt.
    ays = input("\n\nare you sure you want to shut down AOS? (all unsaved documents will be lost) [Y/N] ")    
    if ays == "N":
        print("\n"*4)
        startup()
    elif ays == "Y":
        shutdown()
    else:
        print("wat. plz rsrt ur AOs nouw")
                


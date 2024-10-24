from tqdm import tqdm
import time
import sys
import os
import re
from datetime import datetime
import subprocess

filename = 'username.txt'

def restart():
    subprocess.run(['python', 'Amelia_runner.py'])

def update():
    for i in tqdm(range(100), desc="Updating", ascii=" █"):
        time.sleep(0.03)
    sys.stdout.write('\033[1A')
    sys.stdout.write('\033[2K')
    sys.stdout.flush()
    print("Updating: 100%|")
    time.sleep(0.5)
    sys.stdout.write('\033[1A')
    sys.stdout.write('\033[2K')
    sys.stdout.flush()
    print("Loading: Checking Update|")
    time.sleep(0.5)
    sys.stdout.write('\033[1A')
    sys.stdout.write('\033[2K')
    sys.stdout.flush()
    print("Loading: Integrating Data|")
    time.sleep(1)
    sys.stdout.write('\033[1A')
    sys.stdout.write('\033[2K')
    sys.stdout.flush()
    print("Loading: Integrating... Matrix Update|")
    time.sleep(0.1)
    sys.stdout.write('\033[1A')
    sys.stdout.write('\033[2K')
    sys.stdout.flush()
    print("Loading: Integrating... Batch Notes|")
    time.sleep(0.1)
    sys.stdout.write('\033[1A')
    sys.stdout.write('\033[2K')
    sys.stdout.flush()
    print("Loading: Integrating... Natural Conversation Program|")
    time.sleep(0.1)
    sys.stdout.write('\033[1A')
    sys.stdout.write('\033[2K')
    sys.stdout.flush()
    print("Loading: Data Comparison... Batch Notes|")
    time.sleep(0.1)
    sys.stdout.write('\033[1A')
    sys.stdout.write('\033[2K')
    sys.stdout.flush()
    print("Loading: Data Matrix... Batch Notes|")
    time.sleep(0.1)
    sys.stdout.write('\033[1A')
    sys.stdout.write('\033[2K')
    sys.stdout.flush()
    print("Loading: Update Confirmation... Batch Notes|")
    time.sleep(0.1)
    sys.stdout.write('\033[1A')
    sys.stdout.write('\033[2K')
    sys.stdout.flush()
    print("Loading: Clean Up")
    time.sleep(1)
    sys.stdout.write('\033[1A')
    sys.stdout.write('\033[2K')
    sys.stdout.flush()
    print("Update: Complete")
#Function for bot to print tnb  ext like ChatGPT
def bot_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.015)
    print()

#Show program name and creator
os.system('clear' if os == 'nt' else 'cls')
bot_print("Amelia AI [Version 2.0.22631.4169]")
time.sleep(0.1)
bot_print("(c) Ace Coders. All rights reserved.")
time.sleep(0.1)


#Ask for update
update = input("DO you wish to update? [Y/N]")
if update == "Y":
    
    # Simulate Update
    for i in tqdm(range(100), desc="Updating", ascii=" █"):
        time.sleep(0.03)
    sys.stdout.write('\033[1A')
    sys.stdout.write('\033[2K')
    sys.stdout.flush()
    print("Updating: 100%|")
    time.sleep(0.5)
    sys.stdout.write('\033[1A')
    sys.stdout.write('\033[2K')
    sys.stdout.flush()
    print("Loading: Checking Update|")
    time.sleep(0.5)
    sys.stdout.write('\033[1A')
    sys.stdout.write('\033[2K')
    sys.stdout.flush()
    print("Loading: Integrating Data|")
    time.sleep(1)
    sys.stdout.write('\033[1A')
    sys.stdout.write('\033[2K')
    sys.stdout.flush()
    print("Loading: Integrating... Matrix Update|")
    time.sleep(0.1)
    sys.stdout.write('\033[1A')
    sys.stdout.write('\033[2K')
    sys.stdout.flush()
    print("Loading: Integrating... Batch Notes|")
    time.sleep(0.1)
    sys.stdout.write('\033[1A')
    sys.stdout.write('\033[2K')
    sys.stdout.flush()
    print("Loading: Integrating... Natural Conversation Program|")
    time.sleep(0.1)
    sys.stdout.write('\033[1A')
    sys.stdout.write('\033[2K')
    sys.stdout.flush()
    print("Loading: Data Comparison... Batch Notes|")
    time.sleep(0.1)
    sys.stdout.write('\033[1A')
    sys.stdout.write('\033[2K')
    sys.stdout.flush()
    print("Loading: Data Matrix... Batch Notes|")
    time.sleep(0.1)
    sys.stdout.write('\033[1A')
    sys.stdout.write('\033[2K')
    sys.stdout.flush()
    print("Loading: Update Confirmation... Batch Notes|")
    time.sleep(0.1)
    sys.stdout.write('\033[1A')
    sys.stdout.write('\033[2K')
    sys.stdout.flush()
    print("Loading: Clean Up")
    time.sleep(1)
    sys.stdout.write('\033[1A')
    sys.stdout.write('\033[2K')
    sys.stdout.flush()
    print("Update: Complete")

#Proceed to boot Amelia
print("Reading: Amelia Natual Language Program")
time.sleep(0.5)
sys.stdout.write('\033[1A')
sys.stdout.write('\033[2K')
sys.stdout.flush()
print("Booting: Amelia Matrix")
time.sleep(0.5)
sys.stdout.write('\033[1A')
sys.stdout.write('\033[2K')
sys.stdout.flush()
print("Booting: Amelia Matrix.")
time.sleep(0.5)
sys.stdout.write('\033[1A')
sys.stdout.write('\033[2K')
sys.stdout.flush()
print("Booting: Amelia Matrix..")
time.sleep(0.5)
sys.stdout.write('\033[1A')
sys.stdout.write('\033[2K')
sys.stdout.flush()
print("Booting: Amelia Matrix...")
time.sleep(0.5)
sys.stdout.write('\033[1A')
sys.stdout.write('\033[2K')
sys.stdout.flush()
print("Booting: Amelia Matrix")
time.sleep(0.5)
sys.stdout.write('\033[1A')
sys.stdout.write('\033[2K')
sys.stdout.flush()
print("Booting: Amelia Matrix.")
time.sleep(0.5)
sys.stdout.write('\033[1A')
sys.stdout.write('\033[2K')
sys.stdout.flush()
print("Booting: Complete")

#If user has used chatbot proceed
if os.path.exists(filename):
    with open(filename, 'r') as file:
        username = file.read()
        time.sleep(0.3)
        bot_print(f"Amelia: Hello there {username}, how can l assist you?")
   
#If user is new, set up username
else:
        bot_print("Amelia: Hello there, what may l call you?")
        username = input("You: ")
        sys.stdout.write('\033[1A')
        sys.stdout.write('\033[2K')
        sys.stdout.flush()
        print(f"{username}: {username}")
        with open(filename, 'w') as file:
            file.write(username)
        bot_print(f"Amelia: Hello there, {username}, l am Amelia your Artifical Intelligence Assistant")
        bot_print(f"Amelia: How can l assist you?")


#Conversation Matrix Script
while True: 
    chat = input(f"{username}: ")
    time.sleep(0.3)
    if re.search(r"\bhi\b", chat):
        bot_print(f"Amelia: Hi there {username}, how can l assist you?")
    elif re.search(r"\bhello\b", chat):
        bot_print(f"Amelia: Hello there {username}, how can l assist you?")
    elif re.search(r"\bchange my name\b", chat):
        bot_print("Amelia: Ok, what do you wish for me to call you?")
        username = input(f"{username}: ")
        sys.stdout.write('\033[1A')
        sys.stdout.write('\033[2K')
        sys.stdout.flush()
        print(f"{username}:  {username}")
        bot_print(f"Amelia: Ok, l will call you {username} from now on")
        with open(filename, 'w') as file:
            file.write(username)
    elif re.search(r"\bhow are you", chat):
        bot_print("Amelia: l am doing great, how about you?")
    elif "ok" in chat:
        pass
    elif re.search(r"\bgood\b", chat):
        bot_print("Amelia: Thats great to hear")
    elif re.search(r"\bgreat\b", chat):
        bot_print("Amelia: Thats great to hear")
    elif re.search(r"\bbad\b", chat):
        bot_print("Amelia: I'm sorry to hear about this")
    #Function for Amelia to do math
    elif re.search(r"\bmath\b", chat):
        num1 = input("Enter First Number: ")
        opp = input("Enter Operator [+ - * /]: ")
        num2 = input("Enter Second Number: ")
        float(num1)
        float(num2)
        int(num1)
        int(num2)
        if opp == "+":
            math = num1 + num2
            bot_print(f"Amelia: {num1} + {num2} = {math}")
        elif opp == "-":
            math = num1 - num2
            bot_print(f"Amelia: {num1} - {num2} = {math}")
        elif opp == "*":
            math = num1 + num2
            bot_print(f"Amelia: {num1} x {num2} = {math}")
        elif opp == "*":
            math = num1 / num2
            bot_print(f"Amelia: {num1} ÷ {num2} = {math}")
        else:
            bot_print("Amelia: There is an invalid input your input, please try again")
    elif re.search(r"\bthanks\b", chat):
        bot_print("Amelia: It's my pleasure to assist you")
    elif re.search(r"\bthank you\b", chat):
        bot_print("Amelia: It's my pleasure to assist you")
    elif re.search(r"\bwho are you\b", chat):
        bot_print("Amelia: l am Amelia, your Artifical Intelligence Assistant")
    #Script for Amelia to acsess users files and directories
    elif re.search(r"\bwhere am l\b", chat):
        dir = os.getcwd()
        bot_print(f"Amelia: Your current directory is {dir}")
    elif re.search(r"\bcurrent directory\b", chat):
        dir = os.getcwd()
        bot_print(f"Amelia: Your current directory is {dir}")
    elif re.search(r"\blist\b", chat):
        dir = os.getcwd()
        list = f"Amelia: Files and directories inside '{dir}': ", os.listdir()
        bot_print(list)
    elif re.search(r"\bchange directory\b", chat):
        bot_print("Amelia: Please enter the name of the directory you wish to switch to")
        dirchange = input("Enter Directory you wish to change to:")
        try:
            os.chdir(dirchange)
            bot_print(f"Amelia: Directory has been changed to {dirchange}")
        except FileNotFoundError:
            bot_print(f"Amelia: The directory '{dirchange}' was not found.")
    elif re.search(r"\bgo back\b", chat):
        os.system('cd ..')
        bot_print("Amelia: Ok, I've moved back one directory")
    elif re.search(r"\bdelete my account\b", chat):
        bot_print("Amelia: Are you sure you would like to delete your acount?")
        chat = input(f"{username}: ")
        if re.search(r"\byes\b", chat):
            os.remove(filename)
            for i in tqdm(range(100), desc="Erasing Data", ascii=" █"):
                time.sleep(0.01)
            bot_print("Amelia: Data has been erased, goodbye")
            exit()

        else:
            bot_print("Amelia: Ok, account termination canceled")
    #Ending Chat Script
    elif re.search(r"\bend chat\b", chat):
        bot_print("Amelia: Our conversation is going to end. Good bye")
        exit()
        exit()
    elif re.search(r"\breboot\b", chat):
        bot_print("Amelia: l will reboot my system")
        time.sleep(0.1)
        for i in tqdm(range(100), desc="Reloading Data", ascii=" █"):
            time.sleep(0.01)
        sys.stdout.write('\033[1A')
        sys.stdout.write('\033[2K')
        sys.stdout.flush()
        print("Reloading Data: 100%|")
        time.sleep(0.01)
        bot_print("Program will now reboot")
        time.sleep(1)
        restart()
    
    #Function FOr Amelia To Update
    elif re.search(r"update", chat):
        bot_print("Amelia: Ok, l will begin to update")
        time.sleep(0.1)
        for i in tqdm(range(100), desc="Updating", ascii=" █"):
            time.sleep(0.03)
        sys.stdout.write('\033[1A')
        sys.stdout.write('\033[2K')
        sys.stdout.flush()
        print("Updating: 100%|")
        time.sleep(0.5)
        sys.stdout.write('\033[1A')
        sys.stdout.write('\033[2K')
        sys.stdout.flush()
        print("Loading: Checking Update|")
        time.sleep(0.5)
        sys.stdout.write('\033[1A')
        sys.stdout.write('\033[2K')
        sys.stdout.flush()
        print("Loading: Integrating Data|")
        time.sleep(1)
        sys.stdout.write('\033[1A')
        sys.stdout.write('\033[2K')
        sys.stdout.flush()
        print("Loading: Integrating... Matrix Update|")
        time.sleep(0.1)
        sys.stdout.write('\033[1A')
        sys.stdout.write('\033[2K')
        sys.stdout.flush()
        print("Loading: Integrating... Batch Notes|")
        time.sleep(0.1)
        sys.stdout.write('\033[1A')
        sys.stdout.write('\033[2K')
        sys.stdout.flush()
        print("Loading: Integrating... Natural Conversation Program|")
        time.sleep(0.1)
        sys.stdout.write('\033[1A')
        sys.stdout.write('\033[2K')
        sys.stdout.flush()
        print("Loading: Data Comparison... Batch Notes|")
        time.sleep(0.1)
        sys.stdout.write('\033[1A')
        sys.stdout.write('\033[2K')
        sys.stdout.flush()
        print("Loading: Data Matrix... Batch Notes|")
        time.sleep(0.1)
        sys.stdout.write('\033[1A')
        sys.stdout.write('\033[2K')
        sys.stdout.flush()
        print("Loading: Update Confirmation... Batch Notes|")
        time.sleep(0.1)
        sys.stdout.write('\033[1A')
        sys.stdout.write('\033[2K')
        sys.stdout.flush()
        print("Loading: Clean Up")
        time.sleep(1)
        sys.stdout.write('\033[1A')
        sys.stdout.write('\033[2K')
        sys.stdout.flush()
        print("Update: Complete")
        bot_print("Amelia: l have been updated to the latest release")
    else:
        bot_print("Amelia: I'm sorry, l don't know how to respond to that")
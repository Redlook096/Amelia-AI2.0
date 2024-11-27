from tqdm import tqdm
import time
import sys
import os
import re
from datetime import datetime
import subprocess

filename = 'username.txt'
passfile = 'password.txt'

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

#Function for bot to print text like ChatGPT
def bot_print(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.015)
    print()

#Show program name and creator
os.system('clear' if os == 'nt' else 'cls' and "clear")
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
for i in tqdm(range(100), desc="Booting", ascii=" █"):
        time.sleep(0.005)
sys.stdout.write('\033[1A')
sys.stdout.write('\033[2K')
sys.stdout.flush()
print("Booting: 100%|")

#If user has used chatbot proceed
if os.path.exists(filename):
    with open(filename, 'r') as file:
        username = file.read()
        time.sleep(0.3)
        bot_print(f"Amelia: Hello there {username}, please enter your password to login")
        #Ask user to enter password
        with open(passfile, 'r') as file:
            password = file.read()
        security = input("Enter Password: ")
        time.sleep(0.1)
        if security == password:
            sys.stdout.write('\033[1A')
            sys.stdout.write('\033[2K')
            sys.stdout.flush()
            print("Enter Password: ******")
            bot_print(f"Amelia: Hello there {username}, how can l assist you?")
        else:
            bot_print("Amelia: Password is incorrect, program will now end")
            exit()

    
   
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
        #Ask user to create password
        bot_print("Amelia: For your security, please create a password")
        password = input("Enter New Password: ")
        sys.stdout.write('\033[1A')
        sys.stdout.write('\033[2K')
        sys.stdout.flush()
        print("Enter Password: ******")
        with open(passfile, 'w') as file:
            file.write(password)
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
    elif re.search(r"\bwho is this\b", chat):
        bot_print("Amelia: l am Amelia, your Artificual Intelligence assistant")
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
    elif re.search(r"\bdelete my account\b", chat):
        bot_print("Amelia: Are you sure you would like to delete your acount?")
        chat = input(f"{username}: ")
        if re.search(r"\byes\b", chat):
            os.remove(filename)
            os.remove(passfile)
            for i in tqdm(range(100), desc="Erasing Data", ascii=" █"):
                time.sleep(0.01)
            bot_print("Amelia: Data has been erased, goodbye")
            exit()
            exit()
        else:
            bot_print("Amelia: Ok, account termination canceled")
    
    #Sensoring Inappropriate Language
    elif re.search(r"\bfuck\b", chat):
        bot_print("Amelia: Sorry, l cannot respond to that as it goes against my guide lines")
    elif re.search(r"\bdick\b", chat):
        bot_print("Amelia: Sorry, l cannot respond to that as it goes against my guide lines")
    elif re.search(r"\bbitch\b", chat):
        bot_print("Amelia: Sorry, l cannot respond to that as it goes against my guide lines")
    elif re.search(r"\bslut\b", chat):
        bot_print("Amelia: Sorry, l cannot respond to that as it goes against my guide lines")
    elif re.search(r"\bchink\b", chat):
        bot_print("Amelia: Sorry, l cannot respond to that as it goes against my guide lines")
    elif re.search(r"\bass\b", chat):
        bot_print("Amelia: Sorry, l cannot respond to that as it goes against my guide lines")
    elif re.search(r"\bgay\b", chat):
        bot_print("Amelia: Sorry, l cannot respond to that as it goes against my guide lines")
    elif re.search(r"\bnigger\b", chat):
        bot_print("Amelia: Sorry, l cannot respond to that as it goes against my guide lines")
    elif re.search(r"\bshit\b", chat):
        bot_print("Amelia: Sorry, l cannot respond to that as it goes against my guide lines")
    elif re.search(r"\brape\b", chat):
        bot_print("Amelia: Sorry, l cannot respond to that as it goes against my guide lines")
    elif re.search(r"\bcock\b", chat):
        bot_print("Amelia: Sorry, l cannot respond to that as it goes against my guide lines")
    elif re.search(r"\bpenis\b", chat):
        bot_print("Amelia: Sorry, l cannot respond to that as it goes against my guide lines")
    elif re.search(r"\bpussy\b", chat):
        bot_print("Amelia: Sorry, l cannot respond to that as it goes against my guide lines")
    elif re.search(r"\bvigina\b", chat):
        bot_print("Amelia: Sorry, l cannot respond to that as it goes against my guide lines")
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
    elif re.search(r"clear", chat):
         repeat = 0
         while repeat < 6:
            sys.stdout.write('\033[1A')
            sys.stdout.write('\033[2K')
            sys.stdout.flush()
            repeat += 1
         os.system('clear' if os == 'nt' else 'cls' and "clear")

         
    else:
        bot_print("Amelia: I'm sorry, l don't know how to respond to that")

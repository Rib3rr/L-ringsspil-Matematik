from termcolor import colored
from pyfiglet import figlet_format
from colorama import Fore
from math_tasks import math_tasks
from threading import Thread
import random
import time


def Hurtigtest():
    global questions
    global correct
    while True:
            questions += 1
            category = random.choice(MENU_LIST)
            if category == "Addition (plus)":
                correct += math_tasks().task1(random.randint(0, 4))
            elif category == "Subtraktion (minus)":
                correct += math_tasks().task2(random.randint(0, 4))
            elif category == "Ligning":
                correct += math_tasks().task3(random.randint(0, 4))
            elif category == "Multiplikation (gange)":
                correct += math_tasks().task4(random.randint(0, 4))
            elif category == "Division (dividering)":
                correct += math_tasks().task5(random.randint(0, 4))
            else:
                correct += math_tasks().task1(random.randint(0, 4))

MENU_LIST = [
    "Addition (plus)",
    "Subtraktion (minus)",
    "Multiplikation (gange)",
    "Division (dividering)",
    "Ligning",
    "Blandede opgaver",
    "Hurtigtest (60sekunder)",
    "Hurtigtest (30sekunder)"
]

print((colored(figlet_format("Matematik Spil"), color="blue")))
print(" --> Velkommen til matematik spillet!\n")
print(" Vælg en mulighed:\n")

for x,i in enumerate(MENU_LIST, start=1):
    print(' {}[{}] {}{}{}'.format(Fore.RESET,x ,Fore.LIGHTCYAN_EX, i, Fore.RESET))
    
print('\n {}[{}] {}{}{}'.format(Fore.RESET,"X",Fore.RED, "Luk spil", Fore.RESET))

while True:
    user_input = input("\n > ")
    try:
        if user_input == "X" or 1 <= int(user_input) <= int(x):
            break
        else:
            print(Fore.RED+f"Vælg en mulighed imellem 1-{x}!"+Fore.RESET)
    except ValueError:
        print(Fore.RED+"Vælg et nummer!"+Fore.RESET)

if user_input == "X":
    exit()

elif MENU_LIST[int(user_input)-1] == "Hurtigtest (60sekunder)":
        questions = 0
        correct = 0
        Thread(target=Hurtigtest, args=()).start()
        time.sleep(60)
        exit(f"\n Tiden er gået! Du fik {str(Fore.LIGHTCYAN_EX) + str(correct) + str(Fore.RESET)} ud af {str(Fore.LIGHTCYAN_EX) + str(questions) + str(Fore.RESET)} opgaver rigtigt!")

elif MENU_LIST[int(user_input)-1] == "Hurtigtest (30sekunder)":
        questions = 0
        correct = 0
        Thread(target=Hurtigtest, args=()).start()
        time.sleep(30)
        exit(f"\n Tiden er gået! Du fik {str(Fore.LIGHTCYAN_EX) + str(correct) + str(Fore.RESET)} ud af {str(Fore.LIGHTCYAN_EX) + str(questions) + str(Fore.RESET)} opgaver rigtigt!")

else:
    print(f"\n Valgte kategori: " + str(Fore.LIGHTCYAN_EX) + MENU_LIST[int(user_input)-1] + str(Fore.RESET))
    print(" Vælg hvor mange opgaver du vil løse:\n " + str(Fore.YELLOW) + "Du kan vælge følgende muligheder: 5, 10, 25" + str(Fore.RESET))
    while True:
        user_input_2 = input("\n > ")
        if user_input_2.isdigit() and (int(user_input_2) == 5 or int(user_input_2) == 10 or int(user_input_2) == 25):
            break
        else:
            print(Fore.RED+"Vælg et nummer!"+Fore.RESET)
    
    print(f"\n Valgte kategori: " + str(Fore.LIGHTCYAN_EX) + MENU_LIST[int(user_input)-1] + str(Fore.RESET))
    print(f" Valgte antal opgaver: " + str(Fore.LIGHTCYAN_EX) + user_input_2 + str(Fore.RESET))
    if MENU_LIST[int(user_input)-1] == "Addition (plus)":
        correct = 0
        for i in range(int(user_input_2)):
            correct += math_tasks().task1(random.randint(0, 4))
    elif MENU_LIST[int(user_input)-1] == "Subtraktion (minus)":
        correct = 0
        for i in range(int(user_input_2)):
            correct += math_tasks().task2(random.randint(0, 4))
    elif MENU_LIST[int(user_input)-1] == "Ligning":
        correct = 0
        for i in range(int(user_input_2)):
            correct += math_tasks().task3(random.randint(0, 4))
    elif MENU_LIST[int(user_input)-1] == "Multiplikation (gange)":
        correct = 0
        for i in range(int(user_input_2)):
            correct += math_tasks().task4(random.randint(0, 4))
    elif MENU_LIST[int(user_input)-1] == "Division (dividering)":
        correct = 0
        for i in range(int(user_input_2)):
            correct += math_tasks().task5(random.randint(0, 4))
    elif MENU_LIST[int(user_input)-1] == "Blandede opgaver":
        correct = 0
        for i in range(int(user_input_2)):
            category = random.choice(MENU_LIST)
            if category == "Addition (plus)":
                correct += math_tasks().task1(random.randint(0, 4))
            elif category == "Subtraktion (minus)":
                correct += math_tasks().task2(random.randint(0, 4))
            elif category == "Ligning":
                correct += math_tasks().task3(random.randint(0, 4))
            elif category == "Multiplikation (gange)":
                correct += math_tasks().task4(random.randint(0, 4))
            elif category == "Division (dividering)":
                correct += math_tasks().task5(random.randint(0, 4))
            else:
                correct += math_tasks().task1(random.randint(0, 4))

    print(f"\n Du fik {str(Fore.LIGHTCYAN_EX) + str(correct) + str(Fore.RESET)} ud af {str(Fore.LIGHTCYAN_EX) + user_input_2 + str(Fore.RESET)} opgaver rigtigt!")
    
    

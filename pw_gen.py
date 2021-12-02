import random
import pyperclip
import ctypes

ctypes.windll.kernel32.SetConsoleTitleW("flyteam pw generator")



symbol = 0
lower = 0
upper = 0
number = 0
count = 0
password = []

import os

# System call
os.system("")

# Class of different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.GREEN)


length = input('''
                                   ███████╗██╗  ██╗   ██╗████████╗███████╗ █████╗ ███╗   ███╗
                                   ██╔════╝██║  ╚██╗ ██╔╝╚══██╔══╝██╔════╝██╔══██╗████╗ ████║
                                   █████╗  ██║   ╚████╔╝    ██║   █████╗  ███████║██╔████╔██║
                                   ██╔══╝  ██║    ╚██╔╝     ██║   ██╔══╝  ██╔══██║██║╚██╔╝██║
                                   ██║     ███████╗██║      ██║   ███████╗██║  ██║██║ ╚═╝ ██║
                                   ╚═╝     ╚══════╝╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝
                                   
                                   




                                   Wie viele Zeichen? lol (default 128)\n
:''')
length = 128 if length == '' else int(length)




while count < length:
    rand = random.randint (0,3)
    if rand == 0:
        lower += 1
        b = int(random.randint (97,123))
        password.append(b)
    elif rand == 1:
        upper += 1
        b = random.randint (65,91)
        password.append(b)
    elif rand == 2:
        number += 1
        b = random.randint (48,58)
        password.append(b)
    elif rand == 3:
        r = random.randint(0,2)
        symbol += 1
        if r == 0:
            b = random.randint (33,48)
            password.append(b)
        elif r == 1:
            b = random.randint (91,97)
            password.append(b)
        elif r == 2:
            b = random.randint (123,126)
            password.append(b)
    count += 1

word = "".join([chr(c) for c in password])


pyperclip.copy(word)

print ("Random pw of length %s is: \n\n" % length + style.MAGENTA)

#print('******')
print(word + style.GREEN)
#print('******')

#print ("\nIt contains",lower,"lowercase,",upper,"uppercase,",number,"numbers and",symbol,"symbol characters")
input('\n\n\n\nPasswort wurde in deine Zwischenablage pasted... \n\nDrücke Enter um den Generator zu schließen'+ style.GREEN)

import requests
import random
import os
from colorama import Fore
from console.utils import set_title

os.system('color')

def title(text):
    set_title(text)

def namegen():
    length = random.randint(4, 20)
    letters = "il"
    return ''.join(random.choice(letters) for i in range(length))

title('Hidden User Gen By (...)#4953 | Tried: 0 | Taken: 0 | Available: 0')

choice = input(f'{Fore.CYAN}[1] Start\n[2] Exit\n\n'f'{Fore.YELLOW}Choice: ')

tried = 0
used = 0
available = 0

if choice == '1':
    while True:
        name = namegen()
        r = requests.get("https://api.roblox.com/users/get-by-username?username=" + name)
        a = r.text
        if a.find('Id') == -1:
            tried = tried + 1
            available = available + 1
            title('Hidden User Gen By (...)#4953 | Tried: ' + str(tried) + ' | Taken: ' + str(used) + ' | Available: ' + str(available))
            print(f'{Fore.GREEN}[+] ' + name + ' is available')
            open("usernames.txt", "a").write(name + '\n')
        else:
            tried = tried + 1
            used = used + 1
            title('Hidden User Gen By (...)#4953 | Tried: ' + str(tried) + ' | Taken: ' + str(used) + ' | Available: ' + str(available))

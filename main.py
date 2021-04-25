import requests
import random
import os
from colorama import Fore
from console.utils import set_title
from discordwebhook import Discord

os.system('color')

def title(text):
    set_title(text)

def namegen():
    length = random.randint(4, 20)
    letters = "Il"
    return ''.join(random.choice(letters) for i in range(length))

title('Hidden User Gen By (...)#4953 | Tried: 0 | Taken: 0 | Available: 0')

choice = input(f'{Fore.CYAN}[1] Start\n[2] Exit\n\n'f'{Fore.YELLOW}Choice: ')

tried = 0
taken = 0
available = 0

if choice == '1':
    while True:
        name = namegen()
        r = requests.get("https://api.roblox.com/users/get-by-username?username=" + name)
        a = r.text
        if a.find('Id') == -1:
            tried = tried + 1
            available = available + 1
            title('Hidden User Gen By (...)#4953 | Tried: ' + str(tried) + ' | Taken: ' + str(taken) + ' | Available: ' + str(available))
            print(f'{Fore.GREEN}[+] ' + name + ' is available')
            open("usernames.txt", "a").write(name + '\n')
            discord = Discord(url="https://discord.com/api/webhooks/123/abc")
            discord.post(
    embeds=[
        {
            "title": "Hidden User Gen",
            "description": "Found A New User!",
            "fields": [
                {"name": "Username:", "value": name},
            ],
            "footer": {
                "text": "By (...)#4953",
                "icon_url": "https://cdn.discordapp.com/avatars/747719812054253568/7fc895c7e52f0e68b916476b40325923.png?size=256",
            },
        }
    ],
)

        else:
            tried = tried + 1
            taken = taken + 1
            title('Hidden User Gen By (...)#4953 | Tried: ' + str(tried) + ' | Taken: ' + str(taken) + ' | Available: ' + str(available))

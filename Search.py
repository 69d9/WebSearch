import requests
import random, string
import re
from sys import exit
from colorama import Fore

print(rf"""
{Fore.YELLOW}
    Coded By GhosT LulzSec
    Telegram : @WW6WW6WW6
    GitHub: https://github.com/69d9
    All rights reserved.

            o  o   o  o
         |\/ \^/ \/|  
         |,-------.|  
       ,-.(|)   (|),-. 
       \_*._ ' '_.* _/  
        /-.--' .-`\  
   ,--./    `---'    \,--. 
   \   |(  )     (  )|   /  
hjw \  |         |  /  
`97  \ | /|\     /|\ | /  
     /  \-._     _,-/  \  
    //| \  `---'  // |\\  
   /,-.,-.\       /,-.,-.\  
  o   o   o      o   o    o  
""")

search = input("Enter your search : ")
try:
    number = int(input("how many websits you want? "))
except Exception as err:
    print("\033[0;31;40m" , err)
    exit(0)

if " " in search:
    search = search.replace(" ", "+")

url = f"https://ahmia.fi/search/?q={search}"

with open("user-agents.txt", "r+") as a: 
    users = random.choice(a.readlines()).strip()  

header = {
    "User-Agent": users
}

results_limt = number
result_collected = 0

webs = requests.get(url, headers=header).text
reg = r"\w+\.onion"
data = re.findall(reg, webs)
filename = ''.join(random.choice(string.ascii_letters + string.digits)for i in range(5))
data = list(dict.fromkeys(data))

with open(f"{filename}.txt", "a+") as f:
    for i in data:
        if result_collected >= results_limt:
            break  
        i = i + "\n"
        f.write(i)
        result_collected += 1
    print(f"\033[0;31;40m \nCompleted, saved in {filename}.txt")

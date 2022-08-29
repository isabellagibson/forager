import requests
import json
import random
import os
from colorama import init, Fore

from Helper import Helper

DOMAIN_MISFIRE = True
MISFIRE_COUNT = 30
WEBSITES = json.load(open('websites.json', 'r'))
ALL_DOMAINS = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

init()
clear_screen()

print(f'{Fore.LIGHTGREEN_EX}Downloading all TLDs...{Fore.RESET}')
open('tlds.json', 'w').write(json.dumps([ln.lower() for ln in requests.get('https://data.iana.org/TLD/tlds-alpha-by-domain.txt').text.split('\n')][1:], indent=2))
clear_screen()
print(f'Loaded domains: {Fore.LIGHTGREEN_EX}{str(len(WEBSITES))}{Fore.RESET}')

cnt = input(f'How many times do you want to create a mistype for each domain? [{str(MISFIRE_COUNT)}] ')
if cnt != '':
    MISFIRE_COUNT = int(cnt)

for website in WEBSITES:
    for i in range(MISFIRE_COUNT):
        delim = random.randint(0, (len(website) - 1))
        layout_index = Helper.QWERTY_LAYOUT.index(website[delim])
        dlm = (layout_index - random.choice([1, -1]))
        if dlm < 0:
            dlm = 0
        if dlm > 25:
            dlm = 25
        dlm = Helper.QWERTY_LAYOUT[dlm]
        misfired = website[0:delim] + dlm + website[(delim + 1):]
        if misfired not in ALL_DOMAINS:
            ALL_DOMAINS.append(misfired)

clear_screen()
print(f'Foraged {Fore.LIGHTGREEN_EX}{str(len(ALL_DOMAINS))}{Fore.RESET} websites.')

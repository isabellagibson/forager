import json
import requests
import random
from colorama import init, Fore

PROXIES_URL = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all&simplified=true'
WEBSITES = json.load(open('domains.json', 'r'))
PROXIES = []
REQUEST_TIMEOUT = 10

init()

use_proxies = (input(f'Do you want to use proxies? [Y/n] ').lower() in ['', 'y', 'yes'])
if use_proxies:
    PROXIES = requests.get(PROXIES_URL).text.split('\r\n')[:-1]
print(f'Scanning {Fore.LIGHTGREEN_EX}{str(len(WEBSITES))}{Fore.RESET} websites.')
for w in WEBSITES:
    w = f'http://{w}'
    if use_proxies:
        proxy = random.choice(PROXIES)
        proxies = {
            'http': f'http://{proxy}',
            'https': f'http://{proxy}'
        }
        try:
            req = requests.get(w, timeout=REQUEST_TIMEOUT, proxies=proxies)
            print(req.status_code, w)
        except Exception as e:
            pass
    else:
        try:
            req = requests.get(w, timeout=REQUEST_TIMEOUT)
            print(req.status_code, w)
        except Exception as e:
            pass
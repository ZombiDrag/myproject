import requests
from datetime import datetime
import time

def log(text):
    
    now = str(datetime.now())
    s = open("log.txt", "a")
    s.write(now + ": " + text + "\n")
    s.close()

f = open("sites.txt", "r")
sites = f.readlines()
f.close()


for site in sites:
    
    site = site.strip()
    if site == "":
        continue

    try:
        response = requests.get(site)
    except:
        print(f"Сайт не существует {site}. Сервер не работает .")
        log(f"Сайт не существует {site}. Сервер не работает .")
        continue

    if response.status_code == 200:
        print(f"Сайт работает {site}")
        log(f"Сайт работает {site}")
    else:
        print(f"Сайт не работает {site}. Код ошибки:{response.status_code}")
        log(f"Сайт не работает {site}. Код ошибки:{response.status_code}")
print(f"Проверка завершена!Сайты {", ".join(sites)}.")
log(f"Проверка завершена!Сайты {", ".join(sites)}.")


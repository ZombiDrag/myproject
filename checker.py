import requests
from datetime import datetime
import time

def log(text):
    
    now = str(datetime.now())
    s = open("log.txt", "a")
    s.write(now + ": " + text + "\n")
    s.close()

sites =["https://google.com","https://wikipedia.org",
                                "https://github.com",
  "https://this-is-a-fake-and-broken-domain-123.com",
               "https://broken-website-test-link.net"]


for site in sites:
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


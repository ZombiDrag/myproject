import requests
import sys

try:
    response = requests.get("https://goog879le.com")
except:
    print("Сайт не сущетвует. Сервер не работает .")
    sys.exit()
if response.status_code == 200:
    print("Сайт работает ")
else:
    print(f"Сайт не работает Код ошибки:{response.status_code}")
print("Проверка завершена!")
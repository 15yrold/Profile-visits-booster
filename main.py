import os
import logging
import requests
import threading
from colorama import Fore

successful = 0
failed = 0
threadcount = 0
codes = [200, 201, 204]
log = logging.info
logging.basicConfig(
    level = logging.INFO,
    format = f'{Fore.LIGHTBLUE_EX}[{Fore.RESET}%(asctime)s{Fore.LIGHTBLUE_EX}] %(message)s{Fore.RESET}',
    datefmt = '%H:%M:%S'
)
os.system('cls')
link_of_view_counter = input('Enter link: ')
amount_of_views = int(input('\nAmount of views: '))

def cls():
    os.system('cls')

def title_change():
    os.system('title Successful: {} Failed: {}'.format(successful, failed))

def main():
    cls()
    global successful
    global failed
    for i in range(int(amount_of_views)):
        try:
            r = requests.get(link_of_view_counter)
            if r.status_code in codes:
                successful = successful + 1
                title_change()
                log(f'Successfully sent request. {Fore.LIGHTBLUE_EX}|{Fore.GREEN} Worked: {Fore.LIGHTGREEN_EX}{successful} {Fore.LIGHTBLUE_EX}| {Fore.RED}Failed: {Fore.LIGHTRED_EX}{failed}')
        except:
            failed = failed + 1
            title_change()
            log(f'Failed to send request. {Fore.LIGHTBLUE_EX}|{Fore.GREEN} Worked: {Fore.LIGHTGREEN_EX}{successful} {Fore.LIGHTBLUE_EX}| {Fore.RED}Failed: {Fore.LIGHTRED_EX}{failed}')

def start_threading():
    for i in range(int(threadcount)):
        threading.Thread(target = main).start()

def settings():
    global threadcount
    threading = input('\nUse Threads? (Y/N): ')
    if threading == 'Y' or threading == 'y' or threading == 'Yes' or threading == 'yes':
        amount_of_threads = int(input('\nAmount of Threads: '))
        threadcount = amount_of_threads
        start_threading()
    elif threading == 'N' or threading == 'n' or threading == 'No' or threading == 'no':
        main()

if __name__ == '__main__':
    settings()

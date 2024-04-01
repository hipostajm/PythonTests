#Simple lan ip scan with DB

import threading
import sqlite3
from ping3 import ping
import socket

try:
    con = sqlite3.connect("./AutoPing/AutoPing.db")
except:
    con = sqlite3.connect("./AutoPing.db")

cur = con.cursor()

cur.execute('Drop table if exists IPs')

cur.execute('Drop table if exists Ports')

cur.execute(
"""
    Create table if not exists IPs(
            id INTEGER Primary key autoincrement
            , IP TEXT
            , Status TEXT
    )
""")

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('192.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
 
local_ip = get_local_ip().split('.')

ip_base = f"{local_ip[0]}.{local_ip[1]}.{local_ip[2]}."
ip_list = {}

threads_number = 255 #its better to use only but you dont need to (it will be slower) 1, 3, 5, 15, 17, 51, 85, 255
thread_divider = int(255/threads_number)

def Scan(from_ip,to_ip):
    for i in range(from_ip,to_ip):

        ip=ip_base+str(i)
        r = ping(ip)

        if type(r) == float:
            r = "Good"
        elif r == False:
            r = "No Response"
        else:
            r = "Time out"

        ip_list[ip]=r

        print(f"{ip} | {r}")

check = 0
threads = []

for i in range(threads_number):
    if check == 0:
        thread = threading.Thread(target=Scan, args=(1,thread_divider))
    else:
        thread = threading.Thread(target=Scan, args=(thread_divider*i,thread_divider*(i+1)))
    check += 1
    threads.append(thread)

if threads_number != 1 or 3 or 5 or 15 or 17 or 51 or 85 or 255:
    thread = threading.Thread(target=Scan, args=((int(255/threads_number)*threads_number), 256))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()



for i in ip_list:
    cur.execute("Insert into IPs (IP, Status) values (?,?)",(i,ip_list[i]))
    con.commit()

con.close
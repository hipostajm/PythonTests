#Simple lan ip scan with DB

import threading
import sqlite3
from ping3 import ping

con = sqlite3.connect("./AutoPing/AutoPing.db")

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
# cur.execute(
# """
#     Create table if not exists Ports(
#             id INTEGER Primary key autoincrement
#             , Port TEXT
#             , IP TEXTs
#             , Status TEXT
#     )
# """)

ip_base = '192.168.1.'

threads_number = 51 #use only 1, 3, 5, 15, 17, 51, 85, 255
thread_divider = int(255/threads_number)

ip_list = []
response_list = []

def Scan(From,To):
    for i in range(From,To):

        ip=f'{ip_base}{i}'
        r = ping(ip)

        if type(r) == float:
            r = "Good"
        elif r == False:
            r = "No Response"
        else:
            r = "Time out"

        ip_list.append(ip)
        response_list.append(r)

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

Scan(255,256)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

for i in range(255):
    cur.execute("Insert into IPs (IP, Status) values (?,?)",(ip_list[i],response_list[i]))
    con.commit()

con.close
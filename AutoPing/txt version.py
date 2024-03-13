#Simple lan ip scan with txt

import threading
from ping3 import ping

open("./AutoPing/Ips.txt", 'a')
try:
    file = open("./AutoPing/Ips.txt", 'w')
except:
    file = open('./Ips.txt','w')

ip_base = '192.168.1.'

threads_number = 85 #use only 1, 3, 5, 15, 17, 51, 85, 255
thread_divider = int(255/threads_number)

    
def ScanTxT(from_ip,to_ip):
    for i in range(from_ip,to_ip):

        ip=ip_base+str(i)
        r = ping(ip)

        if type(r) == float:
            r = "Good"
        elif r == False:
            r = "No Response"
        else:
            r = "Time out"

        added = f"{ip} | {r}"

        print(added)
        file.write(f'{added}\n')


check = 0
threads = []

for i in range(threads_number):
    if check == 0:
        thread = threading.Thread(target=ScanTxT, args=(1,thread_divider))
    else:
        thread = threading.Thread(target=ScanTxT, args=(thread_divider*i,thread_divider*(i+1)))
    check += 1
    threads.append(thread)

ScanTxT(255,256)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

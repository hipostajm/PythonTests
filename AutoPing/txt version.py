#Simple lan ip scan with txt

import threading
from ping3 import ping

open("./AutoPing/Ips.txt", 'a')
try:
    file = open("./AutoPing/Ips.txt", 'w')
except:
    file = open('./Ips.txt','w')

ip_base = '192.168.1.'

threads_number = 120 #its better to use only but you dont need to (it will be slower) 1, 3, 5, 15, 17, 51, 85, 255
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

if threads_number != 1 or 3 or 5 or 15 or 17 or 51 or 85 or 255:
    thread = threading.Thread(target=ScanTxT, args=((int(255/threads_number)*threads_number), 256))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

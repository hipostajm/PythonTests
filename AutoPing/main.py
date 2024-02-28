import sqlite3
from ping3 import ping, verbose_ping
import nmap

nm = nmap.PortScanner()

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

for i in range(0,255):

    ip=f'192.168.88.{i}'
    r = ping(ip)

    if type(r) == float:
        r = "Good"
    elif r == False:
        r = "No Response"
    else:
        r = "Time out"

    print(ip,' ',r)

    cur.execute("Insert into IPs (IP, Status) values (?,?)",(ip,r))
    con.commit()
# IpList = con.execute("""Select IP from IPs where Status = "Good";""").fetchall()

# for i in IpList:
#     ip = i[0]
#     for port in range(1,65535):

#         nm[ip]['tcp'][port]['state']

#         if r == True:
#             r = 'Good'
#             cur.execute("Insert into Ports (Port, IP ,Status) values (?,?,?)",(port,ip,r))
#             con.commit()
#         else:
#             pass

con.close
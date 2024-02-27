import sqlite3
from ping3 import ping, verbose_ping

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
cur.execute(
"""
    Create table if not exists Ports(
            id INTEGER Primary key autoincrement
            , Port TEXT
            , Status TEXT
    )
""")

for i in range(0,255):

    ip=f'192.168.88.{i}'
    r = ping(ip)

    print(ip,' ',r)

    if type(r) == float:
        r = "Good"
    elif r == False:
        r = "No Response"
    else:
        r = "Time out"

    cur.execute("Insert into IPs (IP, Status) values (?,?)",(ip,r))
    con.commit()
IpList = con.execute("""Select IP from IPs where Status = "Good";""").fetchall()

for i in IpList:
    ip = i[0]
    for port in range(1,65535):
        r = ping(f"{ip}:{port}")

        if type(r) == float:
            r = "Good"
        elif r == False:
            r = "No Response"
        else:
            r = "Time out"

        cur.execute("Insert into Ports (Port, Status) values (?,?)",(port,r))
        con.commit()

con.close
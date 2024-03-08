import threading
import sqlite3
from ping3 import ping

# Establish connection to SQLite database
con = sqlite3.connect("./AutoPing/AutoPing.db")
cur = con.cursor()

# Drop existing tables if they exist
cur.execute('DROP TABLE IF EXISTS IPs')
cur.execute('DROP TABLE IF EXISTS Ports')

# Create 'IPs' table if it does not exist
cur.execute("""
    CREATE TABLE IF NOT EXISTS IPs(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            IP TEXT,
            Status TEXT
    )
""")

# IP base for scanning
ip_base = '192.168.1.'

# Number of threads to use for scanning
threads_number = 85  # Use only 1, 3, 5, 15, 17, 51, 85, 255
thread_divider = int(255 / threads_number)

# Dictionary to store IP statuses after scanning
ip_list = {}

# Function to scan IP addresses
def scan(from_ip, to_ip):
    for i in range(from_ip, to_ip):
        ip = f'{ip_base}{i}'
        response = ping(ip)

        if type(response) == float:
            status = "Good"
        elif response is False:
            status = "No Response"
        else:
            status = "Time out"

        ip_list[ip] = status
        print(f"{ip} | {status}")

# Initialize variables for thread creation
check = 0
threads = []

# Create threads for scanning IP addresses
for i in range(threads_number):
    if check == 0:
        thread = threading.Thread(target=scan, args=(1, thread_divider))
    else:
        thread = threading.Thread(target=scan, args=(thread_divider * i, thread_divider * (i + 1)))
    check += 1
    threads.append(thread)

# Scan the last remaining IPs not covered by threads
scan(255, 256)

# Start all threads for IP scanning
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

# Insert IP scan results into the database
for ip, status in ip_list.items():
    cur.execute("INSERT INTO IPs (IP, Status) VALUES (?, ?)", (ip, status))
    con.commit()

# Close database connection
con.close()

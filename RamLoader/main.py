from os import system
import threading

def youtube_open():
    for _ in range(100):
        system('start https://www.youtube.com')

threads_number = 50
threads = []

for i in range(threads_number):
    thread = threading.Thread(target=youtube_open)
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
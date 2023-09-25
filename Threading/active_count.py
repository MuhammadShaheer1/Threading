import time
import threading
from threading import Thread

def sleepMe(x):
    print("Thread %x going to sleep for 2 seconds." % x)
    time.sleep(2)
    print("Thread %x is active now." % x)

for x in range(10):
    th = Thread(target=sleepMe, args=(x, ))
    th.start()
    print("Current thread count: %x" % threading.active_count())
import threading
import time

def print_1():
    print("Starting of Thread: ", threading.current_thread().name)
    time.sleep(2)
    print("Finishing of Thread: ", threading.current_thread().name)

def print_2():
    print("Starting of Thread: ", threading.current_thread().name)
    print("Finishing of Thread: ", threading.current_thread().name)

a = threading.Thread(target=print_1, name="Thread-1", daemon=True)
b = threading.Thread(target=print_2, name="Thread-2")

a.start()
b.start()
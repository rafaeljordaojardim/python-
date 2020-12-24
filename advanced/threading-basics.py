# Threading allows us to run more than one task at the same time
import threading

import time

def myfunction():
    print("Start a thread")
    time.sleep(3)
    print("End a thread")

threads = []

for i in range(5):
    th = threading.Thread(target = myfunction)
    th.start()
    threads.append(th)

for th in threads:
    th.join()

# course 
    #Threading
    # start() #simply starts or initiates the thread
     
    # join() #makes sure the program waits for all threads to terminate
#using the Thread class form the 'threading' 
# module and telling it the target function to be executed using the 'target' argument
    th = threading.Thread(target = myfunction) 
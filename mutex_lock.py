import threading
import time


def fun1():
    global shared  # make the shared variable global
    print("Thread1 trying to acquire lock")
    lock.acquire()  # thread 1 acquires the lock. Now thread 2 will not be able to acquire the lock until it is unlocked by thread 1
    print("Thread1 acquired lock")
    x = shared  # thread 1 reads value of shared variable
    print("Thread1 reads the value of shared variable as", x)
    x += 1  # thread 1 increments its value
    print("Local updation by Thread1:", x)
    time.sleep(1)  # thread 1 is preempted by thread 2
    shared = x  # thread one updates the value of shared variable
    print("Value of shared variable updated by Thread1 is:",shared)
    lock.release()  # release the lock
    print("Thread1 released the lock")
    
    
def fun2():
    global shared  # make the shared variable global
    print("Thread2 trying to acquire lock")
    lock.acquire()
    print("Thread2 acquired lock")
    y = shared  # thread 2 reads value of shared variable
    print("Thread2 reads the value as", y)
    y -= 1  # thread 2 increments its value
    print("Local updation by Thread2:", y)
    time.sleep(1)  # thread 2 is preempted by thread 1
    shared = y  # thread two updates the value of shared variable
    print("Value of shared variable updated by Thread2 is:",shared)
    lock.release()
    print("Thread2 released the lock")
    
# shared variable
shared = 1
# create a Lock object
lock = threading.Lock()
# create threads
thread1 = threading.Thread(target=fun1)
thread2 = threading.Thread(target=fun2)
# start threads
thread1.start()
thread2.start()
# wait for threads to finish
thread1.join()
thread2.join()
# prints the last updated value of shared variable
print("Final value of shared is", shared)

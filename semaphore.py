import threading
import time


def fun1():
    global shared  # make the shared variable global
    semaphore.acquire()  # acquire the semaphore
    x = shared  # thread 1 reads value of shared variable
    print("Thread1 reads the value as", x)
    x += 1  # thread 1 increments its value
    print("Local updation by Thread1:", x)
    time.sleep(0.01)  # thread 1 is preempted by thread 2
    shared=x    #thread one updates the value of shared variable
    print("ValueofsharedvariableupdatedbyThread1is:",shared)
    semaphore.release()  # release the semaphore

def fun2():
    global shared  # make the shared variable global
    semaphore.acquire()  # acquire the semaphore
    y = shared  # thread 2 reads value of shared variable
    print("Thread2 reads the value as", y)
    y -= 1  # thread 2 increments its value
    print("Local updation by Thread2:", y)
    time.sleep(0.01)  # thread 2 is preempted by thread 1
    shared=y    #thread two updates the value of shared variable
    print("Valueof shared variable updated by Thread2 is:",shared)
    semaphore.release()  # release the semaphore


# shared variable
shared = 1
# create a Semaphore object
semaphore = threading.Semaphore(1)
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
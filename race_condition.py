import threading
import time

shared = 1  # shared variable

def fun1():
    global shared
    x = shared
    print("Thread1 reads the value of shared variable as", x)
    x += 1
    print("Local updation by Thread1:", x)
    time.sleep(1)  # thread one is preempted by thread 2
    shared = x
    print("Value of shared variable updated by Thread1 is:", shared)


def fun2():
    global shared
    y = shared
    print("Thread2 reads the value as", y)
    y -= 1
    print("Local updation by Thread2:", y)
    time.sleep(1)  # thread two is preempted by thread 1
    shared = y
    print("Value of shared variable updated by Thread2 is:", shared)
    

if __name__ == '__main__':
    thread1 = threading.Thread(target=fun1)
    thread2 = threading.Thread(target=fun2)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("Final value of shared is", shared)

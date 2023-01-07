import threading
import time

def thread_function():
    # the work to be done by the thread is defined is defined in this function
    print("Inside Thread")
    for i in range(5):
        print(i)
        time.sleep(1)

def main():
    a_thread = threading.Thread(target=thread_function)   # thread declaration
    a_thread.start()  # thread is created
    a_thread.join()   # process wait for thread to finish.
    print("Inside Main Program")
    for j in range(20, 25):
        print(j)
        time.sleep(1)

if __name__ == "__main__":
    main()
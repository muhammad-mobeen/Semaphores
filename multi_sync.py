import threading

# The resource that the threads will be trying to acquire
resource = []

# Create a lock object to synchronize access to the resource
lock = threading.Lock()

def thread_function(thread_id):
    # Acquire the lock before accessing the resource
    with lock:
        # Append the thread id to the resource
        resource.append(thread_id)
        print(f'Thread {thread_id} acquired the lock and added its id to the resource')


if __name__ == '__main__':
    instances = 5   # Number of thread instances

    # Create two threads
    threads = []
    for i in range(instances):
        t = threading.Thread(target=thread_function, args=(i,))
        threads.append(t)

    # Start the threads
    for t in threads:
        t.start()

    # Wait for the threads to finish
    for t in threads:
        t.join()

    # Print the final state of the resource
    print(f'Final state of the resource: {resource}')
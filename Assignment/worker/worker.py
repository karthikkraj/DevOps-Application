import time

def do_work():
    while True:
        # Simulate doing some background work
        print("Worker Service: Processing a task...")
        time.sleep(10)

if __name__ == '__main__':
    do_work()


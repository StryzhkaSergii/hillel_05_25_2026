import time

def do_something(counter):
    for _ in range(counter):
        print("Sending requests to server...")
        time.sleep(2) #чекати 2 секунди
        print("end of sending")
        yield "request was successfull"


for result in do_something(5):
    print(result)
import threading
import time
NUM =0
def addone():
    global NUM
    NUM += 1
    time.sleep(2)
    print(NUM)

for i in range(10):
    t = threading.Thread(target= addone)
    t.start()


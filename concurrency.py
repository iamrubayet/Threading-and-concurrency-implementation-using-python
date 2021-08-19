import threading
import time


def func():
    print('ran')
    time.sleep(1)
    print("done")
    time.sleep(2)
    print("now done",end=" ")


x = threading.Thread(target=func)
x.start()
print(threading.activeCount())
time.sleep(5)
print("finally\n")

    

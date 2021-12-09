import time
import datetime as dt

a = 1

while a == 1:
    ct = dt.datetime.now().strftime("(%d %b. %Y %H:%M:%S): ")
    print(ct, "Hello, world!")
    time.sleep(5)

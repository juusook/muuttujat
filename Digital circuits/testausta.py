import time

while True:
    clock = time.localtime()
    print(clock.tm_hour, ':', clock.tm_min, ':', clock.tm_sec)
    time.sleep(1)
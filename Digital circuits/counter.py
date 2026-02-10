import time
from time import sleep

#counter
counter = 0
while True:
    #counter = (counter +1) if counter < 7 else 0 #if, else ehto  muuttujan määrittelyssä
    counter = (counter + 1) % 8
    time.sleep(0.5)
    print(counter)
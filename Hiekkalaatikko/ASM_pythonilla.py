from machine import Pin
import time


class Lamp:
    def __init__(self):
        self.button = Pin(7, Pin.IN, Pin.PULL_UP)
        self.led = Pin(20, Pin.OUT)

        self.delay = 0.5
        self.state = self.OFF

    def execute(self):
        self.state()


    def OFF(self):
        self.led.value(0)
        time.sleep(self.delay)
        if self.button.value() == 0:
            self.state = self.ONW
        else:
            self.state = self.OFF


    def Wait(self):
        self.led.value(1)
        time.sleep(self.delay)
        if self.button.value() == 1:
            self.state = self.ON
        else:
            self.state = self.Wait



    def ON(self):
        self.led.value(1)
        time.sleep(self.delay)
        if self.button.value() == 0:
            self.state = self.Wait2
        else:
            self.state = self.ON


    def Wait2(self):
        self.led.value(0)
        time.sleep(self.delay)
        if self.button.value() == 1:
            self.state = self.OFF
        else:
            self.state = self.Wait2


# Pääohjelma
asmLamp = Lamp()
while True:
    asmLamp.execute()

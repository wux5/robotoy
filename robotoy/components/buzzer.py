from gpiozero import Buzzer as ZeroBuzzer
from . import pins
from time import sleep


class Buzzer(ZeroBuzzer):
    def __init__(self):
        super().__init__(pins.BUZZER, initial_value=True)

    # The on/off is reverse from the parent
    def on(self):
        return super().off()

    def off(self):
        return super().on()

    def whistle(self):
        self.on()
        sleep(0.5)
        self.off()

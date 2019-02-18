from gpiozero import OutputDevice
from . import pins


class Fan(OutputDevice):
    def __init__(self):
        super().__init__(pins.FAN, False)

    @property
    def is_working(self):
        return self.value

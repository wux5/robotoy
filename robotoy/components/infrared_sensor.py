from gpiozero import LineSensor
from . import pins


class InfraredSensorLeft(LineSensor):
    def __init__(self):
        super().__init__(pins.INFRARED_LEFT)


class InfraredSensorRight(LineSensor):
    def __init__(self):
        super().__init__(pins.INFRARED_RIGHT)

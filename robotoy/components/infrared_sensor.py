from gpiozero import LineSensor
from . import pins
from ..singleton import singleton


@singleton
class InfraredSensorLeft(LineSensor):
    def __init__(self):
        super().__init__(pins.INFRARED_LEFT)


@singleton
class InfraredSensorRight(LineSensor):
    def __init__(self):
        super().__init__(pins.INFRARED_RIGHT)

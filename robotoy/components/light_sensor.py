from gpiozero import LightSensor
from . import pins
from ..singleton import singleton


@singleton
class LightSensorLeft(LightSensor):
    def __init__(self):
        super().__init__(pins.LIGHT_LEFT)


@singleton
class LightSensorRight(LightSensor):
    def __init__(self):
        super().__init__(pins.LIGHT_RIGHT)

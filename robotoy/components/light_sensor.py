from gpiozero import LightSensor
from . import pins

class LightSensorLeft(LightSensor):
    def __init__(self):
        super().__init__(pins.LIGHT_LEFT)

class LightSensorRight(LightSensor):
    def __init__(self):
        super().__init__(pins.LIGHT_RIGHT)

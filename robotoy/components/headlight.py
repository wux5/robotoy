from gpiozero import RGBLED
from .. import pins
from ..singleton import singleton


@singleton
class Headlight(RGBLED):
    def __init__(self):
        super().__init__(pins.LED_R, pins.LED_G, pins.LED_B)

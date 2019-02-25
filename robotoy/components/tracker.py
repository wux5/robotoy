from .. import pins
from gpiozero import GPIODevice
from ..singleton import singleton


@singleton
class Tracker():
    def __init__(self):
        self.left1_sensor = GPIODevice(pins.TRACK_LEFT_1)
        self.left2_sensor = GPIODevice(pins.TRACK_LEFT_2)
        self.right1_sensor = GPIODevice(pins.TRACK_RIGHT_1)
        self.right2_sensor = GPIODevice(pins.TRACK_RIGHT_2)

from gpiozero import DistanceSensor
from . import pins


class UltraSonic(DistanceSensor):
    def __init__(self):
        super().__init__(echo=pins.ULTRASONIC_ECHO, trigger=pins.ULTRASONIC_TRIGGER)

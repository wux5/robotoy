from gpiozero import AngularServo
from . import pins
from ..singleton import singleton


@singleton
class SearchLightServo(AngularServo):
    def __init__(self):
        super().__init__(pins.SEARCHLIGHT_SERVO)

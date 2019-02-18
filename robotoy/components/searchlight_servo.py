from gpiozero import AngularServo
from . import pins


class SearchLightServo(AngularServo):
    def __init__(self):
        super().__init__(pins.SEARCHLIGHT_SERVO)

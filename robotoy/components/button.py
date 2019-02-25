from gpiozero import Button as ZeroButton
from .. import pins
from ..singleton import singleton


@singleton
class Button(ZeroButton):
    def __init__(self, pin=pins.BUTTON):
        super().__init__(pin)

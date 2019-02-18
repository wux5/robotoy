from gpiozero import PWMLED
from . import pins


class SearchLight():
    def __init__(self):
        self.led_red = PWMLED(pins.LED_R)
        self.led_green = PWMLED(pins.LED_G)
        self.led_blue = PWMLED(pins.LED_B)

    def change_color(self, red, green, blue):
        self.led_red.value = red / 255.0
        self.led_green.value = green / 255.0
        self.led_blue.value = blue / 255.0

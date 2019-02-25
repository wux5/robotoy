from .. import sensors
from ..components.headlight import Headlight
from signal import pause
from time import sleep

s = sensors.UltrasonicSensor()
led = Headlight()

while True:
    if s.distance < 1:
        print(s.distance)
    if s.in_range:
        print(s.next_turn())
        break
    sleep(0.3)


def on():
    led.on()


def off():
    led.off()


# NOTE: when these events are bind, the distance and in_range will stop working
s.when_in_range = on
s.when_out_of_range = off

pause()

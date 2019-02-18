from ..components.infrared_sensor import InfraredSensorLeft, InfraredSensorRight
from signal import pause

left = InfraredSensorLeft()
right = InfraredSensorRight()


def left_on():
    print("Left On")


def left_off():
    print("Left Off")


left.when_activated = left_off
left.when_deactivated = left_on


def right_on():
    print("Right On")


def right_off():
    print("Right Off")


right.when_activated = right_off
right.when_deactivated = right_on

pause()

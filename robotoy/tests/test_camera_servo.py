from ..components.camera_servo import CameraServo
from signal import pause
from time import sleep

s = CameraServo()

s.turn_left(90)
sleep(1)
s.turn_right(90)
sleep(1)
s.turn_up(90)
sleep(1)
s.turn_down(90)
sleep(1)
s.turn_left(0)
s.turn_up(0)

angle = -90
while True:
    if (angle >= 90):
        s.turn_left(0)
        s.turn_up(0)
        sleep(1)
        exit(0)
    s.turn_left(angle)
    s.turn_up(angle)
    angle += 10
    sleep(0.3)

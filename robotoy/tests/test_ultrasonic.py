from ..components.ultrasonic import UltraSonic
from time import sleep

s = UltraSonic()
while True:
    print('Distance: ', s.distance * 100)
    sleep(1)

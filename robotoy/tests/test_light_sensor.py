from ..components.light_sensor import LightSensorLeft, LightSensorRight
from time import sleep

left = LightSensorLeft()
right = LightSensorRight()


while True:
    print('Left:', left.value, 'Right:', right.value)
    sleep(1)

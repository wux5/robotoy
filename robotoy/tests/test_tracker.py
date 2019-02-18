from ..components.tracker import Tracker
from time import sleep

t = Tracker()

while True:
    print(t.left1_sensor.value)

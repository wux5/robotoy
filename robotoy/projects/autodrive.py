from ..components.robot import Robot
from .. import sensors
from ..components.headlight import Headlight
from time import sleep
from ..components.sound import play

robot = Robot()
us = sensors.UltrasonicSensor()
infraredLeft = sensors.InfraredSensorLeft()
infraredRight = sensors.InfraredSensorRight()
light = Headlight()

last_turn = None
red = (1, 0, 0)
green = (0, 1, 0)
blue = (0, 0, 1)


def turn(dir=None):
    global last_turn
    robot.stop()
    if dir is None:
        dir = us.next_turn(last_turn)

    if us.distance < 0.3:
        robot.backward(0.2)
        sleep(0.2)

    if dir == "left":
        robot.left(0.2)
    else:
        robot.right(0.2)
    last_turn = dir
    sleep(0.2)
    print("turn " + last_turn)
    while us.in_range:
        sleep(0.1)

    print(us.distance)
    robot.forward(0.2)


def run():
    while True:
        if not infraredLeft.value:
            print("infrared left")
            light.color = blue
            turn("right")
        elif not infraredRight.value:
            print("infrared right")
            light.color = blue
            turn("left")
        elif us.in_range:
            print("ultrasonic in range")
            light.color = red
            turn()
        else:
            light.color = green
            robot.forward(0.1)
        sleep(0.1)

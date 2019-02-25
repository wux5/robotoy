from robotoy.components.robot import Robot
from robotoy.components.searchlight_servo import SearchLightServo
from robotoy.components.ultrasonic import UltraSonic
from robotoy.components.infrared_sensor import InfraredSensorLeft, InfraredSensorRight
from robotoy.components.searchlight import SearchLight
from time import sleep
from robotoy.components.sound import play

robot = Robot()
servo = SearchLightServo()
us = UltraSonic()
infraredLeft = InfraredSensorLeft()
infraredRight = InfraredSensorRight()
light = SearchLight()

last_turn = None
red = (1, 0, 0)
green = (0, 1, 0)
blue = (0, 0, 1)


def turn(dir=None):
    global last_turn
    robot.stop()
    if dir is None:
        if last_turn == "left":
            start, end, step = servo.min_angle, servo.max_angle, 10
        else:
            start, end, step = servo.max_angle, servo.min_angle, -10
        for angle in range(start, end, step):
            servo.angle = angle
            sleep(0.1)
            if not us.in_range:
                print("clear")
                break
        dir = "left" if servo.angle > 0 else "right"

    servo.mid()
    if us.distance < 0.3:
        robot.backward(0.2)
        sleep(0.2)

    if dir == "left":
        play("./sound/i-farted.wav")
        robot.left(0.2)
    else:
        play("./sound/i-love-you-daddy.wav")
        robot.right(0.2)
    last_turn = dir
    sleep(0.2)
    print("turn " + last_turn)
    print(us.in_range)
    while us.in_range:
        sleep(0.1)

    print(us.distance)
    robot.forward(0.2)


def main():
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
            # print("keep going...")
            light.color = green
            robot.forward(0.1)
        sleep(0.1)


if __name__ == "__main__":
    main()

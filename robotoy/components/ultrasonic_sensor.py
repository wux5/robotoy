from gpiozero import DistanceSensor
from .. import pins
from ..singleton import singleton
from .ultrasonic_servo import UltrasonicServo
from time import sleep


@singleton
class UltrasonicSensor(DistanceSensor):
    def __init__(self, *args, **kwargs):
        super().__init__(echo=pins.ULTRASONIC_ECHO,
                         trigger=pins.ULTRASONIC_TRIGGER, *args, *kwargs)
        self._servo = UltrasonicServo()

    def next_turn(self, last_turn=None):
        servo = self._servo
        if last_turn == "left":
            start, end, step = servo.max_angle, servo.min_angle, -20
        else:
            start, end, step = servo.min_angle, servo.max_angle, 20

        servo.min()
        sleep(0.3)
        servo.max()
        sleep(0.3)
        for angle in range(start, end, step):
            servo.angle = angle
            print(angle, self.distance)
            sleep(1)
            if not self.in_range:
                print("clear")
                break
        print(servo.angle)
        dir = "left" if servo.angle > 0 else "right"
        servo.mid()
        return dir

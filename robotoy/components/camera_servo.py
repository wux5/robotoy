from gpiozero import AngularServo
from . import pins


class CameraServo:
    def __init__(self):
        self.servo_v = AngularServo(pins.CAMERA_SERVO_V)
        self.servo_h = AngularServo(pins.CAMERA_SERVO_H)

    def turn_left(self, angle):
        self.servo_h.angle = -1 * angle

    def turn_right(self, angle):
        self.servo_h.angle = angle

    def turn_up(self, angle):
        self.servo_v.angle = angle

    def turn_down(self, angle):
        self.servo_v.angle = -1 * angle

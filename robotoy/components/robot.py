from gpiozero import Robot as ZeroRobot
from . import pins


class Robot(ZeroRobot):
    def __init__(self):
        super().__init__(
            left=(pins.MOTOR_LEFT_FORWARD,
                  pins.MOTOR_LEFT_BACK, pins.MOTOR_LEFT_PWM),
            right=(pins.MOTOR_RIGHT_FORWARD,
                   pins.MOTOR_RIGHT_BACK, pins.MOTOR_RIGHT_PWM)
        )

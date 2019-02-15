from gpiozero import Robot as Robot
import RPi.GPIO as GPIO
from . import pins


class Car(Robot):
    def __init__(self):
        super().__init__(
            left=(pins.MOTOR_LEFT_FORWARD, pins.MOTOR_LEFT_BACK),
            right=(pins.MOTOR_RIGHT_FORWARD, pins.MOTOR_RIGHT_BACK)
        )
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pins.MOTOR_LEFT_PWM, GPIO.OUT, initial=GPIO.HIGH)
        GPIO.setup(pins.MOTOR_RIGHT_PWM, GPIO.OUT, initial=GPIO.HIGH)
        self.pwm_ENA = GPIO.PWM(pins.MOTOR_LEFT_PWM, 2000)
        self.pwm_ENB = GPIO.PWM(pins.MOTOR_RIGHT_PWM, 2000)
        self.pwm_ENA.start(0)
        self.pwm_ENB.start(0)
        self.pwm_ENA.ChangeDutyCycle(100)
        self.pwm_ENB.ChangeDutyCycle(100)

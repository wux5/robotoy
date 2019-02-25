from subprocess import call
from pathlib import Path
from datetime import datetime
from .singleton import singleton
from .components.camera_servo import CameraServo


@singleton
class Camera():
    def __init__(self):
        Path('./captures').mkdir(parents=True, exist_ok=True)
        self._servo = CameraServo()

    def capture(self, filename=None):
        if filename == None:
            filename = datetime.now().strftime("./captures/IMG-%Y-%m-%d-%H-%M-%S.jpg")
        call(["fswebcam", "-r", "1280x720", filename])
        return filename

    @property
    def servo(self):
        return self._servo

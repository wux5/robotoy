from ..components.ultrasonic import UltraSonic
from ..components.searchlight import SearchLight
from signal import pause
from ..components import sound

s = UltraSonic()
led = SearchLight()


def on():
    led.on()
    sound.play("./sound/maybe-next-time.wav", -1)


def off():
    led.off()
    sound.stop()


s.when_in_range = on
s.when_out_of_range = off

pause()

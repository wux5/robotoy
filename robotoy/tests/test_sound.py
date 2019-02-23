from ..components.sound import play
from signal import pause

while True:
    input("go")
    play('./sound/maybe-next-time.wav')

pause()

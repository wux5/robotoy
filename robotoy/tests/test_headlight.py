from ..components.headlight import Headlight
from signal import pause

light = Headlight()

try:
    while True:
        rgb = input("Enter RGB values(for example: 0 0.5 0):")
        rgb = rgb.split(' ')
        try:
            light.color = (float(rgb[0]), float(rgb[1]), float(rgb[2]))
        except:
            pass
except KeyboardInterrupt:
    print("Good bye.")
    pass

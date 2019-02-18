from ..components.searchlight import SearchLight
from signal import pause

light = SearchLight()

try:
    while True:
        rgb = input("Enter RGB values(for example: 0 100 0):")
        rgb = rgb.split(' ')
        try:
            light.change_color(int(rgb[0]), int(rgb[1]), int(rgb[2]))
        except:
            pass
except KeyboardInterrupt:
    print("Good bye.")
    pass

from pygame import mixer
from time import sleep

# To make this work, make sure the user is in group: audio, bluetooth
# also the user must have a file .asoundrc in the home directory with
# default bluetooth device, see docs/.asoundrc that works for my letv speaker
# https://www.sigmdel.ca/michel/ha/rpi/bluetooth_02_en.html


def play(file):
    try:
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()
        while mixer.music.get_busy() == True:
            sleep(0.5)
    finally:
        mixer.quit()

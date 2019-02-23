from pygame import mixer
from time import sleep

# To make this work, make sure the user is in group: audio, bluetooth
# also the user must have a file .asoundrc in the home directory with
# default bluetooth device, see docs/.asoundrc that works for my letv speaker
# https://www.sigmdel.ca/michel/ha/rpi/bluetooth_02_en.html


def play(file, count=0):
    try:
        if not mixer.get_init():
            mixer.init()
        mixer.music.load(file)
        mixer.music.play(count)
    except Exception as ex:
        print(ex)


def stop():
    if mixer.get_init():
        mixer.quit()

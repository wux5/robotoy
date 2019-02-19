from time import sleep
from ..components.fan import Fan
from ..components.button import Button

fan = Fan()
button = Button()

fan.on()
sleep(1)
fan.off()
print('Press button to turn on/off.')

try:
    while True:
        button.wait_for_active()
        button.wait_for_inactive()  # wait for the button to be released to start

        if (fan.is_working):
            fan.off()
        else:
            fan.on()

except KeyboardInterrupt:
    fan.off()
    pass

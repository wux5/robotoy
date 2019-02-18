from ..components.fan import Fan
from ..components.button import Button

fan = Fan()
button = Button()

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

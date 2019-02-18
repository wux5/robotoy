from ..components.searchlight_servo import SearchLightServo

servo = SearchLightServo()

while True:
    action = input("Where to go:")
    action = action.split(' ')
    sign = (action[0] == "left")
    servo.angle = sign * int(action[1])

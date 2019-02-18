from ..components.robot import Robot
from time import sleep

car = Robot()

print('forward')
car.forward(0.1)
sleep(1)

print('stop')
car.stop()
sleep(0.2)

print('backward')
car.backward(0.1)
sleep(1)
car.stop()

print('left')
car.left(0.2)
sleep(1)

print('forward')
car.forward(0.2)
sleep(1)

print('bye')

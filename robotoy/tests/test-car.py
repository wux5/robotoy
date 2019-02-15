from ..components.car import Car
from time import sleep

car = Car()

print('forward')
car.forward(0.1)
sleep(2)

print('stop')
car.stop()
sleep(2)

print('backward')
car.backward(0.1)
sleep(2)

print('bye')

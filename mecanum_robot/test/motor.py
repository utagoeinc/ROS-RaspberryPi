from gpiozero import Motor
from time import sleep

mt = Motor(19, 13)

mt.forward(0.5)
sleep(3)
mt.stop()
sleep(1)
mt.backward(0.5)
sleep(3)
mt.stop()
import RPi.GPIO as GPIO
from time import sleep

class RotaryEncoder():
    
    def __init__(self, pins):
        self.clk_pin = pins[0]
        self.dt_pin = pins[1]
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pins, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.counter = 0
        self.clk_last_state = GPIO.input(pins[0])

    def countRotary(self):
        self.clk_state = GPIO.input(self.clk_pin)
        self.dt_state = GPIO.input(self.dt_pin)
        if self.clk_state != self.clk_last_state:
            if self.dt_state != self.clk_last_state:
                self.counter += 1
            else:
                self.counter -= 1
            self.is_changed = True
        else:
            self.is_changed = False
        self.clk_last_state = self.clk_state


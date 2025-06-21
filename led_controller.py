# LedController.py
from machine import Pin

class LedController:
    def __init__(self, pin):
        self.led = Pin(pin, Pin.OUT)
        self.off()  # Estado inicial apagado

    def toggle(self):
        self.led.value(not self.led.value())

    def on(self):
        self.led.value(1)

    def off(self):
        self.led.value(0)
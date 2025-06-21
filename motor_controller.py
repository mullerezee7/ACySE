# motor_controller.py
from machine import Pin

class MotorController:
    def __init__(self, in1_pin, in2_pin):
        self.in1 = Pin(in1_pin, Pin.OUT)
        self.in2 = Pin(in2_pin, Pin.OUT)
        self.stop()  # Estado inicial

    def adelante(self):
        self.in1.on()
        self.in2.off()

    def atras(self):
        self.in1.off()
        self.in2.on()

    def stop(self):
        self.in1.off()
        self.in2.off()

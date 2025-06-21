from machine import Pin, PWM
from config import *

class ServoController:
    def __init__(self, pin):
        self.servo = PWM(Pin(pin), freq=50)
        self.move(NEUTRAL)  # Inicia en neutro
    
    def _angle_to_duty(self, angle):
        """Convierte ángulo (0-180) a duty cycle"""
        return int((angle * (125 - 25)) / 180 + 25)
    
    def move(self, angle):
        """Mueve el servo al ángulo especificado"""
        self.servo.duty(self._angle_to_duty(angle))
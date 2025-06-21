from machine import Pin
import bluetooth
from ble import BLEUART  
from servo_controller import ServoController
from led_controller import LedController
from motor_controller import MotorController
import config

#IZQUIERDA: !B705 ----
#DERECHA: !B804 ----
#ADELANTE: !B507 ----
#ATRAS: !B606
#1: !B11: -----
#2: !B219 -----
#3: !B309 -----
#4: !B408 -----

def main():
    # Hardware
    servo = ServoController(config.SERVO_PIN)
    led = LedController(config.LED)
    motor = MotorController(config.IN1, config.IN2)
    
    # Configuración BLE
    BLE_NAME = "Banano"
    print(BLE_NAME, " Conectado")
    ble = bluetooth.BLE()
    uart = BLEUART(ble, BLE_NAME)
    
    def on_ble_command():
        cmd = uart.read().decode().strip()
        print("Comando:", cmd)
        
        if cmd == "!B507":
            motor.adelante()
            
        if cmd == "!B606":
            motor.atras()
            
        if cmd == "!B219":
            motor.stop()
            
        if cmd == "!B804":
            servo.move(config.RIGHT)
            
        if cmd == "!B705":
            servo.move(config.LEFT)
            
        if cmd == "!B11:":
            servo.move(config.NEUTRAL)

        if cmd == "!B408":
            led.on()
        if cmd == "!B309":
            led.off()
        
    uart.irq(handler=on_ble_command)
    print(f"{BLE_NAME} listo!")

if __name__ == "__main__":
    main()
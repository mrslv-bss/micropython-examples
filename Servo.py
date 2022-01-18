from machine import Pin, PWM, ADC
import utime


pot = ADC(Pin(28))  # Potentiometer
servo = PWM(Pin(0))  # Servo
servo.freq(50)


while True:
    value = int(1350 + (pot.read_u16()/9.57)) # scales 0-65535 to 1350-8200
    servo.duty_u16(value) # duty_u16 == 1350 - zero degrees, 8200 - 180 degrees
    utime.sleep(0.02)

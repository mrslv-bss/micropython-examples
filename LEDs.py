from machine import Pin, ADC
from utime import sleep


L1 = Pin(2, Pin.OUT)
L2 = Pin(3, Pin.OUT)
L3 = Pin(4, Pin.OUT)
L4 = Pin(5, Pin.OUT)
LEDS = [L1, L2, L3, L4]
pot = ADC(Pin(28))  # Potentiometer


while True:
    for x in LEDS:
        x.high()
        sleep(pot.read_u16()/32768)
        x.low()

from machine import Pin, PWM
from utime import sleep

buzzer = PWM(Pin(15))
buzz = {"low": 500, 
        "pre-middle": 1000, 
        "middle": 1500, 
        "high": 2000
        }
iteration = ['high', 'middle', 'low', 'high', 'pre-middle', 'low', 'low']


def sound(freq, volume=5000, delay=0.1):
    buzzer.freq(freq)
    buzzer.duty_u16(volume)
    sleep(delay)
    buzzer.duty_u16(0)
    sleep(delay)


for k in iteration:
    sound(buzz[k])
    print(buzz[k])

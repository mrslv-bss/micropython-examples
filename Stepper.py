from machine import Pin
import utime

pin_a = Pin(0, Pin.OUT)
pin_b = Pin(1, Pin.OUT)
pin_c = Pin(2, Pin.OUT)
pin_d = Pin(3, Pin.OUT)

mode = 'acw'
rotate = [[1, 0, 0, 1], [1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 1, 1]]


def rotater(step, delay):
    pin_a.value(step[0])
    pin_b.value(step[1])
    pin_c.value(step[2])
    pin_d.value(step[3])
    utime.sleep(delay)


while True:
    if mode == 'cw':
        for step in rotate:
            rotater(step, 0.02)
    elif mode == 'acw':
        for step in reversed(rotate):
            rotater(step, 0.02)

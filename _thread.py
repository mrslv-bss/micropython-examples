from machine import Pin
from utime import sleep
import _thread


led_one = Pin(2, Pin.OUT)
led_two = Pin(3, Pin.OUT)
#sync = _thread.allocate_lock()

def ledtwo():
    while True:
        #sync.acquire()
        led_two.value(1)
        sleep(2)
        led_two.value(0)
        sleep(2)
        #sync.release()

_thread.start_new_thread(ledtwo, ())

while True:
    #sync.acquire()
    led_one.value(1)
    sleep(0.5)
    led_one.value(0)
    sleep(0.5)
    #sync.release()

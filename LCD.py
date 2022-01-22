import utime
from machine import I2C
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd
# https://github.com/T-622/RPI-PICO-I2C-LCD


# Settings
I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20

i2c = I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000)
lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS)
# Settings


lcd.clear()  # clear screen
lcd.move_to(0,0)  # cursor position
lcd.putstr('First & Row')  # enter the text
lcd.move_to(7,1)
lcd.putstr('& Second')
lcd.show_cursor()
lcd.blink_cursor_on()  # cursor blinking
utime.sleep(3)
lcd.display_off()  # text display
lcd.backlight_off()  # screen light

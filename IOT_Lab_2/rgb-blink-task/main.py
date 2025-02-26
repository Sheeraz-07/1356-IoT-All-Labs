
from machine import Pin
from neopixel import NeoPixel
import time

Pin = Pin(48, Pin.OUT)   # set GPIO48  to output to drive NeoPixel
neo = NeoPixel(Pin, 1)   # create NeoPixel driver on GPIO48 for 1 pixel
for i in range(50):
    for j in range(70):
        for k in range(20):
            neo[0] = (i, j, k) # set the first pixel to white
            time.sleep(.2)
            neo.write()           
print('hiddim hurrah I did it')
   # write data to all pixels

# from machine import Pin
# from neopixel import NeoPixel
# import time

# pin = Pin(48, Pin.OUT)   # set GPIO48  to output to drive NeoPixel
# neo = NeoPixel(pin, 1)   # create NeoPixel driver on GPIO48 for 1 pixel
# neo[0] = (255, 0, 0) # set the first pixel to white
# time.sleep(.2)
# neo.write()              # write data to all pixels

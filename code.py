from adafruit_circuitplayground.express import cpx
import time

white = (30, 30, 30)
pink = (40, 0, 30)
blue = (0, 0, 50)


while True:
    for i in range (0, 10):
        cpx.pixels[0] = white
        time.sleep(.5)        
        cpx.pixels[1] = pink
        time.sleep(.5)
        cpx.pixels[2] = blue
        time.sleep(.5)
        cpx.pixels[3] = white
        time.sleep(.5)
        cpx.pixels[4] = pink
        time.sleep(.5)
        cpx.pixels[5] = blue
        time.sleep(.5)
        cpx.pixels[6] = white
        time.sleep(.5)
        cpx.pixels[7] = pink
        time.sleep(.5)
        cpx.pixels[8] = blue
        time.sleep(.5)
        cpx.pixels[9] = white
        time.sleep(.5)
        cpx.pixels.fill ((0, 0, 0))

        

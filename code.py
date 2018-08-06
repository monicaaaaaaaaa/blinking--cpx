from adafruit_circuitplayground.express import cpx
import time

white = (30, 30, 30)
pink = (40, 0, 30)
blue = (0, 0, 50)
turquoise = (64, 220, 100)

while True:
    for i in range (0, 10):
        cpx.pixels[0] = white
        time.sleep (.5)
        cpx.pixels[1] = pink
        time.sleep (.5)
        cpx.pixels[2] = turquoise
        time.sleep(.5)
        cpx.pixels[3] = blue
        
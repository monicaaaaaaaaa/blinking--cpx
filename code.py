import time
from adafruit_circuitplayground.express import cpx

white = (30, 30, 30)
pink = (40, 0, 30)
blue = (0, 0, 255)
colors = [white, pink, blue, white, pink, blue, white, pink, blue, white]
while True:
    for i in range(0, 10):
        cpx.pixels[i] = colors[i]
        time.sleep(.5)
        
    for i in range(0, 10):
        cpx.pixels[i] = (0, 0, 0)
        time.sleep(.5)


        

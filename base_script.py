import time 
import numpy
import mss
from yeelight import Bulb

mon = {"top": 40, "left": 0, "width": 800, "height": 640}

sct = mss.mss()

bulb = Bulb("192.168.0.186")

while True:
    start_time = time.time()

    mean = numpy.asarray(sct.grab(mon)).reshape(512000,4).mean(axis=0)
    print(int(mean[2]),int(mean[1]),int(mean[0]))
    try:
        bulb.set_rgb(int(mean[2]),int(mean[1]),int(mean[0]))
    except Exception as e:
        print(str(e))
    elapsed_time = time.time() - start_time
    print(elapsed_time)
    time.sleep(0.5)
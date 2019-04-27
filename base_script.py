import time 
import numpy
import mss
from yeelight import Bulb

sct = mss.mss()

bulb = Bulb("192.168.0.186")

while True:
    start_time = time.time()

    tmp_print = sct.grab(sct.monitors[0])

    mean = numpy.reshape(tmp_print.pixels,(tmp_print.width*tmp_print.height,3)).mean(axis=0)
    print(int(mean[0]),int(mean[1]),int(mean[2]))
    bulb.set_rgb(int(mean[0]),int(mean[1]),int(mean[2]))
    elapsed_time = time.time() - start_time
    print(elapsed_time)
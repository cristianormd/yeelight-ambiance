import time 
import numpy
import mss
import yeelight
from yeelight import Bulb

ERROR_STR = "No Bulb available. Please make sure they are connected. If the issue persists, turn them off and on, and wait 5 seconds before attempting to run this program again."

def assert_connect_bulbs():
    infos = yeelight.discover_bulbs()

    bulbs = []

    for info in infos:
        bulbs.append(yeelight.Bulb(info['ip']))
    if(len(bulbs) == 0):
        raise yeelight.BulbException(ERROR_STR)

    return bulbs

bulbs = assert_connect_bulbs()

mon = {"top": 40, "left": 0, "width": 800, "height": 640}
sct = mss.mss()

while True:
    start_time = time.time()

    mean = numpy.asarray(sct.grab(mon)).reshape(512000,4).mean(axis=0)
    print(int(mean[2]),int(mean[1]),int(mean[0]))
    try:
        for bulb in bulbs:
            bulb.set_rgb(int(mean[2]),int(mean[1]),int(mean[0]))
    except Exception as e:
        print(str(e))
        bulbs = assert_connect_bulbs()

    elapsed_time = time.time() - start_time
    print(elapsed_time)
    time.sleep(0.5)

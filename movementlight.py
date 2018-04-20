# Add your Python code here. E.g.
from microbit import *

noMovementTimer = 20

while True:
    accX = abs(accelerometer.get_x())
    accY = abs(accelerometer.get_y())
    accZ = abs(accelerometer.get_z())
    rotX = abs(compass.get_x())
    rotY = abs(compass.get_y())
    rotZ = abs(compass.get_z())
    
    sleep(250)
    accX = abs(accX - abs(accelerometer.get_x()))
    accY = abs(accY - abs(accelerometer.get_y()))
    accZ = abs(accZ - abs(accelerometer.get_z()))
    rotX = abs(rotX - abs(compass.get_x()))
    rotY = abs(rotY - abs(compass.get_y()))
    rotZ = abs(rotZ - abs(compass.get_z()))
    
    acc = accX + accY + accZ
    rot = rotX + rotY + rotZ
    
  #  if acc > 48:
  #      display.scroll("ac = " + str(acc))
  #  if rot > 3100:
  #      display.scroll("ro = " + str(rot))
        
    if acc <= 48 and rot <= 3100:
        if noMovementTimer == 0:
            display.clear()
        else:
            noMovementTimer = noMovementTimer-1
        sleep(250)
    else:
        for x in range(0,5):
            for y in range(0,5):
                display.set_pixel(x, y, 9)
        noMovementTimer = 20
        sleep(10000)
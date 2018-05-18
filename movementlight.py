# Add your Python code here. E.g.
from microbit import *

# how many times to check there's no more movement
noMovementTimer = 20

while True:
    # get current acceleration and rotation states
    accX = abs(accelerometer.get_x())
    accY = abs(accelerometer.get_y())
    accZ = abs(accelerometer.get_z())
    rotX = abs(compass.get_x())
    rotY = abs(compass.get_y())
    rotZ = abs(compass.get_z())
    
    sleep(250)
    # get acceleration and rotation difference after sleep time
    accX = abs(accX - abs(accelerometer.get_x()))
    accY = abs(accY - abs(accelerometer.get_y()))
    accZ = abs(accZ - abs(accelerometer.get_z()))
    rotX = abs(rotX - abs(compass.get_x()))
    rotY = abs(rotY - abs(compass.get_y()))
    rotZ = abs(rotZ - abs(compass.get_z()))
    
    # sum for all three axes
    acc = accX + accY + accZ
    rot = rotX + rotY + rotZ
    
    # display values above threshold which will trigger led's
#  if acc > 48:
#      display.scroll("ac = " + str(acc))
#  if rot > 3100:
#      display.scroll("ro = " + str(rot))

    # check if acceleration and rotation is below threshold
    # thresholds were determined by empirical tests
    if acc <= 48 and rot <= 3100:
        # switch off light if there was no movement after multiple checks
        if noMovementTimer == 0:
            pin0.write_digital(0)
        else:
            noMovementTimer = noMovementTimer-1
        sleep(250)
    else:
        pin0.write_digital(1)
        noMovementTimer = 20
        sleep(10000)


# test program for the gimbal control module
# gimbal pins are 32 and 33 for pan and tilt, respectively

# run from the main directory

from context import Gimbal
import time

def main():
    test_gimbal = Gimbal(32,33)
    
    while(1):
        test_gimbal.pan(-90)
        test_gimbal.tilt(-90)
        time.sleep(0.5)
        test_gimbal.pan(0)
        test_gimbal.tilt(0)
        time.sleep(0.5)
        test_gimbal.pan(90)
        test_gimbal.tilt(90)
        time.sleep(0.5)


main()
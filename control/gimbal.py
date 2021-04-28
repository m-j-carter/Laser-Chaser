## Michael Carter
## github.com/m-j-carter
## mjcarter@ualberta.ca
## April 2021


# Gimbal control class
# Transcribed from my original arduino code so that it can all be run on the Pi
# This will probably have less reliable motion than sending serial commands to 
# an arduino since it has to run on top of linux, but it's one less device.
# I can always change it later 

import RPi.GPIO as GPIO

class Gimbal:
    def __init__(self, pan_pin, tilt_pin):
        
        self.__pan_pin = pan_pin
        self.__tilt_pin = tilt_pin

        # set GPIO numbering mode
        GPIO.setmode(GPIO.BOARD)
        # initialize the servos
        self.__pan_servo = Servo(pan_pin)
        self.__tilt_servo = Servo(tilt_pin)







    def pan(self, angle):
        # Pan to an absolute angle, in degrees.
        #   0 <-- straight ahead
        # -90 <-- full left
        #  90 <-- full right



    def tilt(self, angle):
            # Tilt to an absolute angle, in degrees.
            #   0 <-- straight ahead
            # -90 <-- full down
            #  90 <-- full up








# Turn servo1 to 90
servo1.ChangeDutyCycle(7)
time.sleep(0.5)
servo1.ChangeDutyCycle(0)




class Servo:
    # Objects of this class represent either the pan or tilt servo.
    # This class handles all servo functionality and GPIO calls. 

    # servo PWMs are the duty cycle on a 20ms clock frequency (50Hz); 
    # all angles are in degrees ranging from -90deg to 90 deg.
    pwm_min = 5     # 5% DC; 1ms <-- -90deg
    pwm_max = 10     # 10% DC; 2ms <-- 90deg

    def __init__(self, pin):
        self.__pin = pin
        # setup the pin mode and GPIO function
        GPIO.setup(self.__pin, GPIO.OUT)
        self.__servo = GPIO.PWM(self.__pin, 50)
        # Start PWM running on the servo, value of 0 (pulse off)
        self.__servo.start(0)



    def move(self, angle):
        # move the servo to the specified angle in degrees
        self.__servo.ChangeDutyCycle(self.__deg_to_pwm(angle))


    def __deg_to_pwm(self, angle):
        # calculates and returns the PWM duty cycle as an int for
        # a specified angle in degrees.
        # angle <-- -90deg to 90deg
        # PWM DC <-- 5% to 10%
        return angle / 36 + 7.5
        

##  Michael Carter         ##
##  github.com/m-j-carter  ##
##  mjcarter@ualberta.ca   ##
##  April 2021             ##


import RPi.GPIO as GPIO

class Gimbal:
    # Gimbal control class
    #   Transcribed from my original arduino code so that it can all be run on the Pi
    #   This will probably have less reliable motion than sending serial commands to 
    #   an arduino since it has to run on top of linux, but it's one less device.
    #   I can always change it later 

    # Since the servo angles will only update if they have changed, 
    # theoretically jitter won't be a problem. 

    def __init__(self, pan_pin, tilt_pin):
        self._pan_pin = pan_pin
        self._tilt_pin = tilt_pin

        # set GPIO numbering mode
        GPIO.setmode(GPIO.BOARD)
        # initialize the servos
        self._pan_servo = Servo(pan_pin)
        self._tilt_servo = Servo(tilt_pin)

    def pan(self, angle):
        # Pan to an absolute angle, in degrees.
        #   0 <-- straight ahead
        # -90 <-- full left
        #  90 <-- full right
        if self._pan_servo.get_angle() != angle:
            self._pan_servo.move(angle)

    def tilt(self, angle):
        # Tilt to an absolute angle, in degrees.
        #   0 <-- straight ahead
        # -90 <-- full down
        #  90 <-- full up
        if self._tilt_servo.get_angle() != angle:
            self._tilt_servo.move(angle)


class Servo:
    # Objects of this class represent either the pan or tilt servo.
    # This class handles all servo functionality and GPIO calls. 

    # servo PWMs are the duty cycle on a 20ms clock frequency (50Hz); 
    # all angles are in degrees ranging from -90deg to 90 deg.
    #PWM_MIN = 5      # 5% DC; 1ms <-- -90deg
    #PWM_MAX = 10     # 10% DC; 2ms <-- 90deg
    MIN_ANGLE = -90  # currently not used in calcs; changing this won't change range
    MAX_ANGLE = 90

    def __init__(self, pin):
        self._pin = pin
        # servo angle ranges from -90deg to 90deg
        self._curr_angle = 0
        # setup the pin mode and GPIO function
        GPIO.setup(self._pin, GPIO.OUT)
        self._servo = GPIO.PWM(self._pin, 50)
        # Start PWM running on the servo, value of 0 (pulse off)
        self._servo.start(0)

    def move(self, angle):
        # move the servo to the specified angle in degrees
        assert Servo.MAX_ANGLE >= angle >= Servo.MIN_ANGLE, "angle must be an integer between %d and %d".format(Servo.MIN_ANGLE, Servo.MAX_ANGLE)
        self._curr_angle = angle
        self._servo.ChangeDutyCycle(self._deg_to_pwm(self.__curr_angle))

    def _deg_to_pwm(self, angle):
        # calculates and returns the PWM duty cycle as an int for a specified angle in degrees.
        # angle <-- -90deg to 90deg
        # PWM DC <-- 5% to 10%
        # adaptable version for different PWMs:
        #   return angle / 36 + PWM_MIN + ((PWM_MAX-PWM_MIN) / 2)     
        return angle / 36 + 7.5

    def get_angle(self):
        # returns an int of the servo's current angle in degrees
        return self._curr_angle
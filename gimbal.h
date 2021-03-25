#ifndef GIMBAL_H
#define GIMBAL_H

#include <Arduino.h>
#include <Servo.h>

#define PAN_SERVO_PIN 2
#define TILT_SERVO_PIN 3

// Gimbal range (degrees)
// Note: arduino's servo library limits range to 0-180 deg
#define PAN_MIN 0
#define PAN_MAX 180
#define TILT_MIN 0
#define TILT_MAX 180

class Gimbal {
//private: 
    Servo servoPan;  
    Servo servoTilt; 

    int panAngle;
    int tiltAngle;

    int panMin, panMax;
    int tiltMin, tiltMax;

public:

    Gimbal();

    void begin();
    void zero();
    void pan(int angle);
    void tilt(int angle);
    void panAbs(int targetAngle);
    void tiltAbs(int targetAngle);
    void update();
    int getPanAngle();
    int getTiltAngle();
    void setPanRange(int min=PAN_MIN, int max=PAN_MAX);
    void setTiltRange(int min=TILT_MIN, int max=TILT_MAX);
};

#endif
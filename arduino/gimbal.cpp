/*  Michael Carter
    github.com/m-j-carter
    mjcarter@ualberta.ca
    March 2021
*/



/*  Changelog:
        - added a begin() method to handle initialization of hardware

*/


/*  Future changes:
        - I'd like to have autoupdate as something you can turn on/off.
        - Should implement some sort of servo angle to gimbal angle ratio

*/


#include "gimbal.h"



void Gimbal::begin() {
    // initializer method to be called from setup()

    // Assign servo pins
    servoPan.attach(PAN_SERVO_PIN);
    servoTilt.attach(TILT_SERVO_PIN);

}

void Gimbal::zero() {
    // move the gimbal to its zero point
    int panAngle = panMax - panMin;
    int tiltAngle = tiltMax - tiltMin;
    // update();
}

void Gimbal::pan(int angle) {
    // pan left/right angle degrees, relative to current position. 
    // - for left, + for right. 
    // assert PAN_MIN <= panAngle + angle <= PAN_MAX
    panAngle += angle;
    // update();
}

void Gimbal::tilt(int angle) {
    // tilt up/down angle degrees, relative to current position. 
    // - for down, + for up. 
    // assert TILT_MIN <= tiltAngle + angle <= TILT_MAX
    tiltAngle += angle;
    // update();
}


void Gimbal::panAbs(int targetAngle) {
    // pan left/right to a target (absolute) angle.
    // - for left, + for right. 
    panAngle = targetAngle;
    // update();
}

void Gimbal::tiltAbs(int targetAngle) {
    // tilt up/down to a target (absolute) angle.
    // - for down, + for up. 
    tiltAngle = targetAngle;
    // update();
}


void Gimbal::update() {
    // Write the current angles to the servos, updating their positions.
    // Should never need to be called externally, but for testing
    // purposes I'm gonna leave it as public.
    servoPan.write(panAngle);
    servoTilt.write(tiltAngle);
}

int Gimbal::getPanAngle() {
    return panAngle;
}

int Gimbal::getTiltAngle() {
    return tiltAngle;
}

// void Gimbal::setPanRange(int min=PAN_MIN, int max=PAN_MAX) {
void Gimbal::setPanRange(int min, int max) {
    panMin = min;
    panMax = max;
}

void Gimbal::setTiltRange(int min, int max) {
    tiltMin = min;
    tiltMax = max;
}



// Gimbal class constructor
Gimbal::Gimbal(void){
 

    // initialize pan/tilt range
    setPanRange();
    setTiltRange();

    // zero the servos
    zero();
}


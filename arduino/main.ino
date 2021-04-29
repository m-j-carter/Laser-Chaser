/*  Michael Carter
    github.com/m-j-carter
    mjcarter@ualberta.ca
    March 2021
*/

#include <math.h>
// #include <array> 
// #include <vector>

#include "gimbal.h"
// using namespace std;

#define PAN_MIN 0
#define PAN_MAX 180
#define TILT_MIN 0
#define TILT_MAX 180



inline int radianToDegree(double radians);
void drawSquare();
void randomMove();
void test();



Gimbal gimbal;   

const int laserPin = 12;
int laserState = LOW;



void setup() {
    pinMode(laserPin, OUTPUT);
    // initialize the gimbal
    gimbal.begin();
    gimbal.setPanRange(PAN_MIN, PAN_MAX);
    gimbal.setTiltRange(TILT_MIN, TILT_MAX);

    laserState = HIGH;
}


void loop() {
    int X = rand() % 400+90;
    int Y = rand() % 400+90;
    int Z = rand() % 400+90;
    // int X = PAN_MAX - PAN_MIN;
    // int Y = TILT_MAX - TILT_MIN;
    drawSquare(X,Y,Z,20);

    update();
    delay(rand() % 500);
}



void randomMove(){
    // generate a random movement within the pan/tilt limits
    int panAngle, tiltAngle;
    panAngle = rand() % PAN_MAX + PAN_MIN;
    tiltAngle = rand() % TILT_MAX + TILT_MIN;
    gimbal.panAbs(panAngle);
    gimbal.tiltAbs(tiltAngle);
}


void update() {
    // update all systems
    digitalWrite(laserPin, laserState);
    gimbal.update();
}






inline int radianToDegree(double radians) {
    // rounds to the nearest integer degree
    return radians * (180.0 / M_PI);
}



void test() {
    // gimbal servo testing
    for (int pos = 0; pos <= 180; pos += 1) {
        gimbal.tiltAbs(pos);
        gimbal.panAbs(pos);
        gimbal.update();
        delay(15);
    }
    
    for (int pos = 180; pos >= 0; pos -= 1) { 
        gimbal.tiltAbs(pos);    
        gimbal.panAbs(pos);
        gimbal.update();
        delay(15);                     
    }
}


void drawSquare(int centerX, int centerY, int centerZ, int radius) {
    // for each point in square[]:
    // 1. calculate pan/tilt angles from the x,y,z components
    // 2. convert to degrees
    // 3. write those angles to the gimbal
    // 4. gimbal.update()

    int sqrCorners[8][3] = { {centerX+radius, centerY+radius, centerZ+radius},        // top-right
                             {centerX+radius, centerY-radius, centerZ+radius},        // bottom-right
                             {centerX-radius, centerY-radius, centerZ+radius},        // bottom-left
                             {centerX-radius, centerY+radius, centerZ+radius},        // top-left
                             {centerX+radius, centerY+radius, centerZ-radius},    
                             {centerX+radius, centerY-radius, centerZ-radius},     
                             {centerX-radius, centerY-radius, centerZ-radius},      
                             {centerX-radius, centerY+radius, centerZ-radius}, };


    for (int i=0; i < 8; i++) {
        double panRads, tiltRads;
        // panRads = atan2(testSquare[i].y, testSquare[i].x);
        // tiltRads = atan2(testSquare[i].z, testSquare[i].x);
        panRads = atan2(sqrCorners[i][1], sqrCorners[i][0]);    // (y,x)
        tiltRads = atan2(sqrCorners[i][2], sqrCorners[i][0]);     // (z,x)

        gimbal.panAbs(radianToDegree(panRads));
        gimbal.tiltAbs(radianToDegree(tiltRads));

        gimbal.update();

        // wait for servos to move
        delay(rand() % 100);
    } 
}


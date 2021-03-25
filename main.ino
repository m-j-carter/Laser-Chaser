/*  Michael Carter
    github.com/m-j-carter
    mjcarter@ualberta.ca
    March 2021
*/

#include <vector>

#include "gimbal.h"
// #include "lib/BasicLinearAlgebra/BasicLinearAlgebra.h"
// #include "lib/Geometry/Geometry.h"

using namespace std;





void drawSquare();
void test();



struct point {
    int x, y, z;
};

std::vector<point>pointmap(4);



Gimbal gimbal;   

void setup() {
    // Initialize the coordinate system 
    int X = 0;
    int Y = 25;
    int Z = 0;

    // initialize the gimbal
    gimbal.begin();

}


void loop() {




}











void drawSquare() {
    //TODO
    return;

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
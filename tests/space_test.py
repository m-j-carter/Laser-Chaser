
# for testing the space class and targing in ordinal space

from context import *
from context import Space
import time

def main():
    
    x_size = 10
    y_size = 10
    z_size = 5

    test_space = Space(x_size, y_size, z_size)

    while 1:
        draw_square(test_space)

    # test_space.set_target_xy_coords(target_x, target_y)




def draw_square(space):
    # corners ordered CCW from top-right
    for target_x, target_y in ( (5,10), (5,0), (-5,0), (-5,10) ):
        print(target_x,target_y)
        # set coords as the target
        space.set_target_xy_coords(target_x, target_y)
        # calculate angles and move to target (handled inside of Space right now)
        space.aim_at_target()

        time.sleep(0.5)




main()
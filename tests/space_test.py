
# for testing the space class and targing in ordinal space

# from context import Gimbal
from context import Space
import time

def main():
    
    x_size = 10
    y_size = 10
    z_size = 10

    test_space = Space(x_size, y_size, z_size)

    test_space.set_target_xy_coords(target_x, target_y)







def draw_square():
    # corners ordered CCW from top-right
    for target_x, target_y in ( (5,5), (5,-5), (-5,-5), (-5,5) ):
        # set coords as the target
        test_space.set_target_xy_coords(target_x, target_y)
        # calculate angles and move to target (handled inside of Space right now)
        test_space.aim_at_target()

        time.sleep(0.5)




main()
##  Michael Carter         ##
##  github.com/m-j-carter  ##
##  mjcarter@ualberta.ca   ##
##  April 2021             ##


# Note: This could theoretically either handle gimbal movements or just return 
# pan/tilt angle values so the calling function could do move the gimbal itself.
# I think that either is probably fine, though the latter might be preferred 
# in the long-term, in case I go back to dedicated hardware for the gimbal control.

# For now, the aim_at_target() and aim_at_point_xy() methods will 
# also handle gimbal movements.


from gimbal import Gimbal
import math




class Space:
    # Space object represents the 3D coordinate space and all the required 
    # targeting/aiming operations within it. 
    
    # coordinate ranges: (-x,x), (0,y), (-z,0)

    # Assumptions:
    #   - the gimbal is centered left to right in the space (x=0)
    #   - targets are only in 2D space, projected on the floor plane (z min)
    #       - this means that the gimbal only ever aims below the horizon
    #   - pan range is limited to 180deg
    #   - the distance units are arbitrary (i think), but must be consistent

    def __init__(self, x_size, y_size, z_height):
        self._limits = Map( x_min = -x_size/2,  \
                            x_max = x_size/2,   \
                            y_min = 0,          \
                            y_max = y_size,     \
                            z_min = -z_height,  \
                            z_max = 0 )

        self._target_coords = Map(x = 0, y = 0)

        # remove this if not making the movements directly 
        self._gimbal = Gimbal(32,33)


    def set_target_xy_coords(self, target_x, target_y):
        # Sets the coordinates of the target in space
        assert self._limits.x_min <= target_x <= self._limits.x_max, "target's X coordinate out of range"
        assert self._limits.y_min <= target_y <= self._limits.y_max, "target's Y coordinate out of range"
        self._target_coords.x = target_x 
        self._target_coords.y = target_y


    def aim_at_target(self):
        # calculates the pan/tilt moves to aim at the target, 
        # then performs the moves. 
        pan_angle = self._calc_pan_angle(self._target_coords.x, self._target_coords.y)
        tilt_angle = self._calc_tilt_angle(self._target_coords.x, self._limits.z_min)

        self._gimbal.pan(pan_angle)
        self._gimbal.tilt(tilt_angle)


    def _calc_pan_angle(self, x, y):
        # Calculates and returns the int pan angle for a specified 
        # x,y point in degrees.
        pan_rads = math.atan2(y, x)
        return int(math.degrees(pan_rads))

    def _calc_tilt_angle(self, x, z):
        # Calculates and returns the int tilt angle for a specified 
        # x,z point in degrees.
        tilt_rads = math.atan2(z, x)
        return int(math.degrees(tilt_rads))









class Map(dict):
    # handy little data object that behaves like a dict
    def __init__(self, **kwargs):
        super(Map, self).__init__(**kwargs)
        self.__dict__ = self
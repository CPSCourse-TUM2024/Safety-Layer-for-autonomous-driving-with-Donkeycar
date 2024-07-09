import numpy as np
import pandas as pd
from math import ceil, floor, sqrt, cos, sin, radians
import random

path = r'car.csv'

# pixels_per_unit = 2


# z = 0, w = 1, x = 0, y = 0
# rotated left 90deg: z = -.5
# rotated right 90deg: z= .5
# initX = 0
# initY = 0
# initZ = 0

size_of_pixel = .5
carCircleHitboxRadius = 12.5 / 2
imu_units_per_map = 2.
cm_per_map = 220.
# matrixCarCircleHitboxRadius = int(carCircleHitboxRadius * unitsPerPixel)


stepForwardSize = 8

stepSideSize = 7
angleSide = 0.0558505
stepSideY = 2.09673
stepSideX = 0.11723

class SafetyData(): # TODO ROMAN I GOT A JOB FOR YOU
    #TODO run the maping and updating of current location
    def __init__(self):
        #cars x and y location given as double as mid of car
        #which is in cms and since the matrix has 0.5cm resolution, the carX and carY should be multiplied by 2 to get the correct index of the matrix.
        # self.matrixCarX = int(self.carX * unitsPerPixel)
        # self.matrixCarY = int(self.carY * unitsPerPixel)
        
        #import 0s and 1s from the csv file into a matrix that is 446 in y and QD by x
        self.A = np.loadtxt(path, delimiter=",", dtype=int)
        
        self.recovery_state = 0

    def convert_to_cm(self, imu_pos: "tuple[float, float]") -> "tuple[float, float]":
        return (
            cm_per_map - imu_pos[1] * cm_per_map / imu_units_per_map,
            imu_pos[0] * cm_per_map / imu_units_per_map
        )
    
    def get_recovery_action(self, state: "tuple[float, float, float, float]"):
        # x, y = self.convert_to_cm(state[:2])
        x, y = state[:2]
        have_collision = self.check_collisions(x, y, carCircleHitboxRadius)
        if self.recovery_state > 0:
            if have_collision and self.recovery_state < 2:
                self.recovery_state = 0
                return None
            else:
                self.recovery_state -= 1
                # print("Recovering", self.recovery_state)
                return (0, -0.5)
        else:
            if have_collision:
                self.recovery_state = 10
                # print("Recovering Start")
                return (0, -1)
            else:
                return None
    
    
    def check_collisions(self, x: float, y: float, r: float) -> bool:
        start_x = max(0, floor((x - r) / size_of_pixel))
        end_x = min(self.A.shape[0]-1, ceil((x + r) / size_of_pixel))
        start_y = max(0, floor((y - r) / size_of_pixel))
        end_y = min(self.A.shape[1]-1, ceil((y + r) / size_of_pixel))

        pixel_radius = size_of_pixel / sqrt(2)

        for x_i in range(start_x, end_x + 1):
            for y_i in range(start_y, end_y + 1):
                if self.A[x_i, y_i] == 1 and \
                    (x - x_i * size_of_pixel) ** 2 + (y - y_i * size_of_pixel) ** 2 <= (r + pixel_radius) ** 2:
                    return True
        return False

import numpy as np
import sys

coordinates = np.ones((446,446), dtype=int)
# coordinates = np.zeros((444,444), dtype=int)
coordinates[2:444, 2:444] = 0

#Car Obstacle
coordinates[88:137, 2:45] = 1

#WaveShareBox
coordinates[188:259, 96:131] = 1


#JumperCableBox
coordinates[2:41, 174:218] = 1

#SmallCableBox
coordinates[326:349, 118:143] = 1

#PiBox
coordinates[242:291, 242:291] = 1

#Center bottom vertical line
coordinates[2:131, 218:228] = 1

#horizontal line
coordinates[342:351, 158:345] = 1

#Vertical line connected to horizontal
coordinates[102:344, 336:345] = 1

# np.set_printoptions(threshold=sys.maxsize)
# print(coordinates)
coordinates = np.flip(coordinates,0)
np.savetxt("foo.csv", coordinates.astype(int), delimiter=",", fmt="%i")

import matplotlib.pyplot as plt

plt.imshow(coordinates)
plt.show()
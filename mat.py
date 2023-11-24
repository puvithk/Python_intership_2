from matplotlib import pyplot as ptl
import numpy as np
import random
x = random.sample([1,2,3,4,5,6,7,8,9],8)
y =random.sample([90,88,76,62,100,20,789,32,74],8)

ptl.scatter(x,y)
ptl.show()
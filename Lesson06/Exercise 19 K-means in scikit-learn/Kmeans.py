import numpy as np
import matplotlib.pyplot as plot
data_points = np.array([
 [1, 1],
 [1, 1.5],
 [2, 2],
 [8, 1],
 [8, 0],
 [8.5, 1],
 [6, 1],
 [1, 10],
 [1.5, 10],
 [1.5, 9.5],
 [10, 10],
 [1.5, 8.5]
])


plot.scatter(data_points.transpose()[0], data_points.transpose()[1])
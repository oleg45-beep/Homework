import numpy as np
linear = np.arange(1, 13)
print(linear.reshape(3, 4))
print(linear.reshape(2,3,2))
print(linear.reshape(3,4).ravel())
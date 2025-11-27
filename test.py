import numpy as np
nums = np.array([12, 45, 2, 78, 31, 5, 96, 14, 67, 23])
L = nums[nums>30]
print(L)
print(nums%2==0)
M = nums.copy()
M[M<10]=-1
print(M)
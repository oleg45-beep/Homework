import numpy as np
scores = np.array([75, 42, 98, 55, 67, 89, 91, 78, 63, 84, 51, 72, 95, 81, 36, 47, 100, 69, 88, 57])
print(scores.mean())
print(min(scores), max(scores))
print(len(scores[scores>=85]))
print(len(scores[scores<60]))
print(np.minimum(scores+5, 100))
import numpy as np
data = np.random.randint(1, 100, 20)
print(data.sum())
print(data.sum()/len(data))
print(min(data), max(data))
print(np.argmax(data))
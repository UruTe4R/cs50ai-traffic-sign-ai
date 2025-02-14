import numpy as np

stats = np.array([[1, 2, 3], [4, 5, 6]])

a= np.min(stats, axis=0)

print(a)
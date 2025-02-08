import numpy as np

array = np.random.normal(loc=0, scale=5**0.5, size=2000)
print(array)
print(np.mean(array))
print(np.var(array))
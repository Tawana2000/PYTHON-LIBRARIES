# Slicing in NumPy follows the same indexing rules as Python lists, but extends them to multiple dimensions, allowing you to select rows, columns , or sub-arrays efficiently.

import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])

print(a[1:4])
print(a[:, 1])
print(a[1:])

# Numpy
# - Create an array with shape (4, 3) of: a. all zeros b. ones c. numbers from 0 to 11
# - Tabulate the following function: F(x)=2x^2+5, x∈[1,100] with step 1.
# - Tabulate the following function: F(x)=e^−x, x∈[−10,10] with step 1.
import numpy as np

a = np.zeros((4, 3))
print(a)

b = np.ones((4, 3))
print(b)

c = np.array([
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [9, 10, 11]
])
print(c)

x = np.arange(1, 101)
x = 2*(x**2)+5
print(x)

y = np.arange(-10, 11)
y = x**0.5-x
print(y)
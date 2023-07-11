# Numpy
# - Create an array with shape (4, 3) of: a. all zeros b. ones c. numbers from 0 to 11
# - Tabulate the following function: F(x)=2x^2+5, x∈[1,100] with step 1.
# - Tabulate the following function: F(x)=e^−x, x∈[−10,10] with step 1.
import numpy as np

a = np.zeros((4, 3))
print(a)

b = np.ones((4, 3))
print(b)

c = np.arange(12).reshape((4,3))
print(c)

x = np.arange(1, 101)
x = 2*(x**2)+5
print(x)

y = np.arange(-10, 11)
# Я взяв значення максимально наближене до e
y = ((1+1/10**6)**(10**6))**-x
print(y)
# i = 1
# n = 14

# while i<n:
#     i = i*2
#     print(i)


import matplotlib.pyplot as plt
from math import floor
import numpy as np

n = list(np.linspace(2, 10))

compute = []
# n = [i for i in range(1, 1700)]

def logfunc(n, count = 0): # look at how this count was used!
    if n==0:
        count+=1
        return 'ok', count
    n = floor(n/2)
    count+=1
    return logfunc(n, count)

for i in n:
     g, c= logfunc(i)
     compute.append(c)

plt.plot(n, compute, marker = 'x')
plt.show()

#
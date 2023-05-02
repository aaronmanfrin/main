import random

import matplotlib.pyplot as plt

v = [0]*50

for i in range(50):
    v[i]= random.randint(0,100)
    plt.xlim(0,50)
    plt.ylim(0,100)
    plt.bar(list(range(50)),v)
    plt.pause(.0001)

plt.show()
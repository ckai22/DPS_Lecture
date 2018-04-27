import numpy as np
import matplotlib.pyplot as plt

particle = np.zeros(1000)
step = range(1000)


for i in range(0, 1000):
    for j in range(1000):        
        r = np.random.rand()
        if r > 0.5:
            particle[j] += 1
        else:
            particle[j] -= 1
    if i%5 == 0:
        plt.cla()
        plt.plot(particle, range(1000), ".")
        plt.pause(0.01)

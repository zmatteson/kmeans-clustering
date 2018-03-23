import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random

data = pd.read_csv('values-output.txt', sep=' ', usecols=[0,1,2], header=None)
data = pd.DataFrame(data)

num_colors = data[2].iloc[-1]
colors = []
print(num_colors)
for _ in range(num_colors+1):
    r = (random.randint(1,100))/100
    b = (random.randint(1,100))/100
    g = (random.randint(1,100))/100

    colors.append([r,b,g])
data[2] = data[2].apply(lambda x: colors[x])

data.plot(kind='scatter', x=0, y=1, c = data[2], s=50)

name = 'k-means-clustering-' + str(1+num_colors)
plt.savefig(name)
plt.show()

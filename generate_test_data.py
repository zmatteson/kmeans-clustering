import random

y, x = random.sample(range(500), 300), random.sample(range(500), 300)

f = open('values.txt', 'w+')

for i in range(300):
    line = str(x[i]) + ' ' + str(y[i]) + '\n'
    f.write(line)

f.close()
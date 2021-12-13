import matplotlib.pyplot as plt
import random

figure = plt.figure()
axes = figure.add_subplot(111)

x = list(range(1,101))
y = []
for i in range(1,101):
    y.append(random.randrange(1,101))
print(y)
axes.bar(x, y, color='g')
axes.plot(x, y, color='r', marker='.')

plt.show()

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1234)

num_sims = 5000
x_random = np.random.rand(num_sims)
y_random = np.random.rand(num_sims)

inside_circle = ((x_random ** 2 + y_random**2) < 1)

print(4*inside_circle.mean())
plt.figure(figsize=[8,5])
n_to_one = np.arange(1, num_sims+1)
plt.plot(n_to_one , 4*inside_circle.cumsum() / n_to_one)
plt.show()
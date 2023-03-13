import numpy as np
import matplotlib . pyplot as plt

data = np.genfromtxt("data.csv", delimiter=",", skip_header=1)

# ---------- a ----------

print("a:", len(data))

# ---------- b ----------

height = data[:, 1]
weight = data[:, 2]
plt.xlabel ('height')
plt.ylabel ('weight')
plt.scatter(height, weight, marker ="o", s=1)
plt.title('b:')
plt.show()

# ---------- c ----------

height_every_50 = data[::50, 1]
weight_every_50 = data[::50, 2]
plt.xlabel ('height')
plt.ylabel ('weight')
plt.scatter(height_every_50, weight_every_50, marker ="o", s=1)
plt.title('c:')
plt.show()

# ---------- d ----------

print("min:", min(height))
print("max", max(height))
print("mean", height.mean())

# ---------- e ----------

males_ind = (data[:,0] == 1)
males_data = data[males_ind]
males_height = males_data[:, 1]

print("male min:", min(males_height))
print("male max", max(males_height))
print("male mean", males_height.mean())

females_ind = (data[:,0] == 0)
females_data = data[females_ind]
females_height = females_data[:, 1]

print("female min:", min(females_height))
print("female max", max(females_height))
print("female mean", females_height.mean())

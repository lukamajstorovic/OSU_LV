import numpy as np
import matplotlib.pyplot as plt

white_square = 255 * np.ones((50, 50))
black_square = np.zeros((50, 50))

column_1 = np.vstack((black_square, white_square))
column_2 = np.vstack((white_square, black_square))

matrix = np.hstack((column_1, column_2))

plt.figure()
plt.imshow(matrix, cmap="gray")
plt.show()

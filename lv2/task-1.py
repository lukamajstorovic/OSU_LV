import numpy as np
import matplotlib.pyplot as plt

x = np.array([1, 3, 3, 2, 1])
y = np.array([1, 1, 2, 2, 1])
plt.plot (x , y , 'b', linewidth =1 , marker =".", markersize =5 )
plt.axis ([0 ,4 ,0 , 4])
plt.show()

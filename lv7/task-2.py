import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as Image
from sklearn.cluster import KMeans

# ucitaj sliku
img = Image.imread("lv7/imgs/test_3.jpg")

# prikazi originalnu sliku
plt.figure()
plt.title("Originalna slika")
plt.imshow(img)
plt.tight_layout()
plt.show()

# pretvori vrijednosti elemenata slike u raspon 0 do 1
img = img.astype(np.float64) / 255

# transfromiraj sliku u 2D numpy polje (jedan red su RGB komponente elementa slike)
w,h,d = img.shape
img_array = np.reshape(img, (w*h, d))

# rezultatna slika
img_array_aprox = img_array.copy()

idx = np.unique(img_array, axis=0)

print('Number of unique colors: ', len(idx))

# podatkovni primjeri

# inicijalizacija algoritma K srednjih vrijednosti
km = KMeans ( n_clusters = 5 , init = 'random', n_init = 5 , random_state = 0 )
# pokretanje grupiranja primjera
km.fit ( img_array )
# dodijeljivanje grupe svakom primjeru
labels = km.predict ( img_array )

centers = km.cluster_centers_

# Replace the values of each data point with the value of its corresponding cluster center
X_replaced = centers[labels]

img_replaced = np.reshape(X_replaced, (w, h, d))

# Convert the img_replaced array back to an image
img_replaced = (img_replaced * 255).astype(np.uint8)

# Display the replaced image
plt.figure()
plt.title("Replaced image")
plt.imshow(img_replaced)
plt.tight_layout()
plt.show()
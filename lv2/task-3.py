import numpy as np
import matplotlib . pyplot as plt
img = plt.imread("road.jpg")
img = img[:, :, 0].copy()
print ( img.shape )
print ( img.dtype )

# ---------- a ----------

plt.figure ()
plt.title('brighter')
plt.imshow (img, cmap ="gray", alpha=0.5)
plt.show ()

# ---------- b ----------

plt.figure ()
plt.title('second half')
split_img = np.hsplit(img, 4)
plt.imshow (split_img[1], cmap ="gray", alpha=1)
plt.show()

# ---------- c ----------

img_rotate = np.rot90(img, 3)
plt.title('rotate 90')
plt.imshow (img_rotate, cmap ="gray", alpha=1)
plt.show()

# ---------- d ----------

plt.title('flip')
plt.imshow (np.fliplr(img), cmap ="gray", alpha=1)
plt.show()

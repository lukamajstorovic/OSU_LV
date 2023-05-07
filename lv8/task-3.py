import numpy as np
from tensorflow import keras
from keras import layers
from matplotlib import pyplot as plt
from PIL import Image

model = keras.models.load_model("lv8/model/model.keras")

image = Image.open("lv8/0.png").convert("L")
image = image.resize((28, 28))

image_array = np.array(image)
image_array = image_array / 255

image_vector = image_array.reshape(1, 784)

prediction = model.predict(image_vector)
predicted_class = np.argmax(prediction)
print("Predicted class:", predicted_class)

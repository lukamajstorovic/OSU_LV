from sklearn import datasets
from sklearn . model_selection import train_test_split
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    mean_absolute_percentage_error,
    r2_score,
)
import matplotlib.pyplot as plt
 #Učitaj podatke
data = pd.read_csv('lv4/data_C02_emission.csv')
#Drop Make, Model
data = data.drop(["Make", "Model"], axis=1)
#Kreiraj X i y
input_variables = ['Fuel Consumption City (L/100km)',
                   'Fuel Consumption Hwy (L/100km)',
                   'Fuel Consumption Comb (L/100km)',
                   'Fuel Consumption Comb (mpg)',
                   'Engine Size (L)',
                   'Cylinders']

output_variables = ['CO2 Emissions (g/km)']
X = data[input_variables].to_numpy()
y = data[output_variables].to_numpy()

#a
X_train , X_test , y_train , y_test = train_test_split (X , y , test_size = 0.2 , random_state =1 )

#b

fig = plt.figure(figsize=(8, 6))
for i in range(0,6):
    plt.scatter(X_train[:,i], y_train, c='blue', label='Training Data', s=1)
    plt.scatter(X_test[:,i], y_test, c='red', label='Test Data', s = 1)
    plt.show()

#c
sc = MinMaxScaler()
X_train_n = sc.fit_transform(X_train)
X_test_n = sc.transform(X_test)



for i in range(0,6):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 6))
    ax1.hist(X_train[:,i], bins=30, color="g")
    ax1.set_title('Histogram of First Column (Original)')

    ax2.hist(X_train_n[:,i], bins=30, color="b")
    ax2.set_title('Histogram of First Column (Normalized)')

    #plt.show()

#d
import sklearn.linear_model as lm

lr_model_n = lm.LinearRegression()
lr_model_n.fit(X_train_n, y_train)

print("Koeficijenti: ", lr_model_n.coef_)
print("Intercept: ", lr_model_n.intercept_)

#e

y_test_p = lr_model_n.predict(X_test_n)

RMSE = mean_squared_error(y_test, y_test_p, squared=False)
MAE = mean_absolute_error(y_test, y_test_p)
MAPE = mean_absolute_percentage_error(y_test, y_test_p)
R2 = r2_score(y_test, y_test_p)

plt.figure()
plt.scatter(x=X_test_n[:, 0], y=y_test, c="b")
plt.scatter(x=X_test_n[:, 0], y=y_test_p, c="r")
plt.show()

print("RMSE: ", RMSE)
print("MAE: ", MAE)
print("MAPE: ", MAPE)
print("R2: ", R2)
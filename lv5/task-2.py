import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

labels = {0: "Adelie", 1: "Chinstrap", 2: "Gentoo"}


def plot_decision_regions(X, y, classifier, resolution=0.02):
    plt.figure()
    # setup marker generator and color map
    markers = ("s", "x", "o", "^", "v")
    colors = ("red", "blue", "lightgreen", "gray", "cyan")
    cmap = ListedColormap(colors[: len(np.unique(y))])

    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(
        np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution)
    )
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.3, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    # plot class examples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(
            x=X[y == cl, 0],
            y=X[y == cl, 1],
            alpha=0.8,
            c=colors[idx],
            marker=markers[idx],
            edgecolor="w",
            label=labels[cl],
        )
    plt.show()


# ucitaj podatke
df = pd.read_csv("lv5/penguins.csv")

# izostale vrijednosti po stupcima
print(df.isnull().sum())

# spol ima 11 izostalih vrijednosti; izbacit cemo ovaj stupac
df = df.drop(columns=["sex"])

# obrisi redove s izostalim vrijednostima
df.dropna(axis=0, inplace=True)

# kategoricka varijabla vrsta - kodiranje
df["species"].replace({"Adelie": 0, "Chinstrap": 1, "Gentoo": 2}, inplace=True)

print(df.info())

# izlazna velicina: species
output_variable = ["species"]

# ulazne velicine: bill length, flipper_length
input_variables = ["bill_length_mm", "flipper_length_mm"]

X = df[input_variables].to_numpy()
y = df[output_variable].to_numpy()
y = y[:, 0]

# podjela train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=123
)

logreg = LogisticRegression()
logreg.fit(X_train, y_train)

print("Koeficijenti:", logreg.coef_)
print("Presječna točka: ", logreg.intercept_)

plot_decision_regions(X_test, y_test, logreg)

from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report,
)

y_test_p = logreg.predict(X_test)

cm = confusion_matrix(y_test, y_test_p)
print("Matrica zabune: ", cm)
disp = ConfusionMatrixDisplay(confusion_matrix(y_test, y_test_p))
disp.plot()
plt.show()

print(classification_report(y_test, y_test_p))
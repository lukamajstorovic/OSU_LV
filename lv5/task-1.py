import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score


X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2,
                            random_state=213, n_clusters_per_class=1, class_sep=1)

# train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=5)

plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap='viridis', label='Training data')

plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap='viridis', marker='x', label='Testing data')

plt.legend()

plt.show()

clf = LogisticRegression(random_state=0)

# Train the model using the training data
clf.fit(X_train, y_train)

# Print the accuracy score for the training and testing data
print(f"Training accuracy: {clf.score(X_train, y_train)}")
print(f"Testing accuracy: {clf.score(X_test, y_test)}")

print("Coefficients:", clf.coef_)
print("Intercept:", clf.intercept_)

b = clf.intercept_[0]
w1, w2 = clf.coef_.T
# Calculate the intercept and gradient of the decision boundary.
c = -b/w2
m = -w1/w2

# Plot the data and the classification with the decision boundary.
xmin, xmax = -4, 4
ymin, ymax = -4, 4
xd = np.array([xmin, xmax])
yd = m*xd + c
plt.plot(xd, yd, 'k', lw=1, ls='--')
plt.fill_between(xd, yd, ymin, color='tab:blue', alpha=0.2)
plt.fill_between(xd, yd, ymax, color='tab:orange', alpha=0.2)

plt.scatter(*X_train[y_train==0].T, s=8, alpha=0.5)
plt.scatter(*X_train[y_train==1].T, s=8, alpha=0.5)
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
plt.ylabel(r'$x_2$')
plt.xlabel(r'$x_1$')

plt.show()

y_pred = clf.predict(X_test)

# Calculate the confusion matrix
cm = confusion_matrix(y_test, y_pred)
print(f"Confusion matrix:\n{cm}")

# Calculate the accuracy, precision, and recall
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")

plt.scatter(X_test[y_test==y_pred, 0], X_test[y_test==y_pred, 1], c='g')
plt.scatter(X_test[y_test!=y_pred, 0], X_test[y_test!=y_pred, 1], c='k')

# Show the plot
plt.show()

# fig, ax = plt.subplots(figsize=(8, 6))
# ax.scatter(X_test[:, 0], X_test[:, 1], c=y_test, cmap='cool', alpha=0.7)

# plt.show()
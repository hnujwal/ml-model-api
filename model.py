import pickle
from sklearn.linear_model import LogisticRegression
import numpy as np

x_train = np.array([[1, 2], [2, 3], [3, 4], [4, 5]])
y_train = np.array([0, 1, 0, 1])
model = LogisticRegression()
model.fit(x_train, y_train)
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
print("Model trained and saved to model.pkl")    
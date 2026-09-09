#Linear regression
import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[1],[2],[3],[4],[5]])
y = np.array([20, 30, 40, 50, 60])

model = LinearRegression()
model.fit(x, y)

prediction = model.predict([[6]])

print(prediction)
print("Coefficient:", model.coef_)
print("Intercept:", model.intercept_)



#Train-Test
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

X = np.array([[1], [2], [3], [4], [5],
              [6], [7], [8], [9], [10]])

y = np.array([20, 30, 40, 50, 60,
              70, 80, 90, 100, 110])

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = LinearRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)# MAE  -> average absolute error
mse = mean_squared_error(y_test, predictions)# MSE -> average squared error

print("MAE:", mae)
print("MSE:", mse)
print("X test:", X_test)
print("Actual:", y_test)
print("Predicted:", predictions)+++
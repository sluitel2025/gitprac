from my_simple_linear_regressor import MySimpleLinearRegressor
import numpy as np

def main():
    object = MySimpleLinearRegressor()
    x_train = [[val] for val in range(0, 100)]
    y_train = [row[0] * 2 + np.random.normal(0, 25) for row in x_train]
    object.fit(x_train, y_train)
    print(object.slope)
    print(object.intercept)

    predicted_y = object.predict([[200], [300]])
    print(predicted_y)
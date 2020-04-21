from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()

# print(iris.feature_names)
# print(iris.target_names)
# print(iris.data)
# print(iris.target)
# print(iris.DESCR)

x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=22)
print(x_train)
print(x_train.shape)
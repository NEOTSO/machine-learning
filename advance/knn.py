from sklearn.neighbors import KNeighborsClassifier

x = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]

estimator = KNeighborsClassifier(n_neighbors=1)

estimator.fit(x, y)

ret = estimator.predict([[0]])
print(ret)

# [0]
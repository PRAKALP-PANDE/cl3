from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score

iris =  load_iris()

x = iris.data
y = iris.target

xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = 0.2, random_state = 42)


class ais:

	def __init__(self, n=10):
		self.knn = KNeighborsClassifier(n_neighbors = n)
	def fit(self, xtrain, ytrain):
		self.knn.fit(xtrain, ytrain)

	def predict (self, xtest):
		return self.knn.predict(xtest)

aiscl = ais(n = 10)

aiscl.fit(xtrain, ytrain)

ypred = aiscl.predict(xtest)

acc = accuracy_score(ytest, ypred)

print(f"Accuracy {acc}")
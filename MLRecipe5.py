from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import random
from scipy.spatial import distance

def euc(a, b):
    return distance.euclidean(a, b)


iris = datasets.load_iris()

class ScrappyKNN():
    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        predictions = []
        for row in X_test:
            label = self.closest(row)
            predictions.append(label)
        return predictions

    def closest(self, row):
        best_dist = euc(row, self.X_train[0])
        best_index = 0
        for i in range(1, len(self.X_train)):
            dist = euc(row, self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.y_train[best_index]

X = iris.data
Y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=.5)

my_classifier1 = KNeighborsClassifier()
my_classifier1.fit(X_train, y_train)
predictions1 = my_classifier1.predict(X_test)
print(predictions1)
print(accuracy_score(y_test, predictions1))

my_classifier2 = DecisionTreeClassifier()
my_classifier2.fit(X_train, y_train)
predictions2 = my_classifier2.predict(X_test)
print(predictions2)
print(accuracy_score(y_test, predictions2))

my_classifier3 = ScrappyKNN()
my_classifier3.fit(X_train, y_train)
predictions3 = my_classifier3.predict(X_test)
print(predictions3)
print(accuracy_score(y_test, predictions3))
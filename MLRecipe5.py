from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

iris = datasets.load_iris()

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
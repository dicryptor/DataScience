from sklearn import datasets
from sklearn import svm

# iris = datasets.load_iris()
digits = datasets.load_digits()

clf = svm.SVC(gamma=0.001, C=100.)

clf = clf.fit(digits.data[:-1], digits.target[:-1])

prediction = clf.predict(digits.data[-1:])

# print(iris)
print(digits)
print(clf)
print(prediction)
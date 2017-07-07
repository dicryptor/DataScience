import matplotlib.pyplot as plt
from sklearn import datasets, svm, metrics

digits = datasets.load_digits()

images_and_labels = list(zip(digits.images, digits.target))
for index, (image, label) in enumerate(images_and_labels[:4]):
    plt.subplot(2, 4, index + 1)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Training: {}'.format(label))

n_samples = len(digits.images)
data = digits.images.reshape((n_samples, -1))

classifer = svm.SVC(gamma=0.001)

classifer.fit(data[:n_samples // 2], digits.target[:n_samples // 2])

expected = digits.target[n_samples // 2:]
predicted = classifer.predict(data[n_samples // 2:])

print("Classification report for classifier {}: \n{}".format(
    classifer, metrics.classification_report(expected, predicted)))
print("Confusion matrix: \n{}".format(metrics.confusion_matrix(expected, predicted)))

images_and_predictions = list(zip(digits.images[n_samples // 2:], predicted))
for index, (image,prediction) in enumerate(images_and_predictions[:4]):
    plt.subplot(2,4,index+5)
    plt.axis('off')
    plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
    plt.title('Prediction: {}'.format(prediction))

plt.show()
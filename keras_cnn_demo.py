import numpy as np
np.random.seed(123)
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten
from keras.layers import Convolution2D, MaxPool2D
from keras.utils import np_utils
from keras.datasets import mnist
from keras import backend as K
K.set_image_dim_ordering("th")
from matplotlib import pyplot as plt

(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

Y_train = np_utils.to_categorical(Y_train, 10)
Y_test = np_utils.to_categorical(Y_test, 10)

print(X_train.shape)
print(Y_train.shape)
# plt.imshow(X_train[0])
# plt.show()

X_train = X_train.reshape(X_train.shape[0], 1, 28, 28)
X_test = X_test.reshape(X_test.shape[0], 1, 28, 28)
X_train = X_train.astype('float32')
X_test = X_test.astype('float32')
X_train /= 255
X_test /= 255

model = Sequential()
model.add(Convolution2D(32, (3,3), activation="relu", input_shape=(1, 28, 28)))

print(model.output_shape)

model.add(Convolution2D(32, (3,3), activation="relu"))
model.add(MaxPool2D(pool_size=(2,2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(128, activation="relu"))
model.add(Dropout(0.25))
model.add(Dense(10, activation="softmax"))

model.compile(loss="categorical_crossentropy",
              optimizer="adam",
              metrics=['accuracy'])

model.fit(X_train, Y_train,
          batch_size=32, epochs=10, verbose=1)

score = model.evaluate(X_test, Y_test, verbose=1)

print(score)

from keras.models import load_model
from keras.preprocessing.image import img_to_array, load_img
import numpy as np
import os

path = 'test\\'
files = os.listdir(path)

img_width, img_height = 150, 150

test_model = load_model('birds.h5')

for file in files:
    img = load_img(os.path.join(path, file),False,target_size=(img_width,img_height))
    x = img_to_array(img)
    x = np.expand_dims(x, axis=0)
    preds = test_model.predict_classes(x)
    prob = test_model.predict_proba(x)
    print(file, preds, prob)
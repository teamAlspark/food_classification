# -*- coding: utf-8 -*-
"""Try1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kG0fJuiZPWzx4jfl4OC9Erd1lhkUnfpH

Code to mount google drive to the Python NoteBook -- To import data set from google drive
"""

from google.colab import drive
drive.mount('/content/drive')

"""Code to unzip the zip file located in the drive"""

from zipfile import ZipFile
file_name = "drive/My Drive/flow_from_big.zip"
with ZipFile(file_name, 'r') as zip:
    zip.extractall()
    print('done')

"""Actual Implementation"""

from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

classifier = Sequential()

classifier.add(Conv2D(32, (3, 3), input_shape = (200, 200, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

classifier.add(Conv2D(32, (3, 3), activation = 'relu'))
classifier.add(MaxPooling2D(pool_size = (2, 2)))

classifier.add(Flatten())

classifier.add(Dense(units = 128, activation = 'relu'))
classifier.add(Dense(units = 15, activation = 'softmax'))

classifier.compile(optimizer = 'adam', loss = 'categorical_crossentropy', metrics = ['accuracy'])

from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(rescale = 1./255,
                                   shear_range = 0.2,
                                   zoom_range = 0.2,
                                   horizontal_flip = True)

test_datagen = ImageDataGenerator(rescale = 1./255)

training_set = train_datagen.flow_from_directory('flow_from_big/training_set',
                                                 target_size = (200, 200),
                                                 batch_size = 32,
                                                 class_mode = 'categorical')

test_set = test_datagen.flow_from_directory('flow_from_big/test_set',
                                            target_size = (200, 200),
                                            batch_size = 32,
                                            class_mode = 'categorical')

classifier.fit_generator(training_set,
                         steps_per_epoch = 12000,
                         epochs = 5,
                         validation_data = test_set,
                         validation_steps = 3000)
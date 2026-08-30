# import numpy as np
# import pandas as pd
# import tensorflow as tf
# from tensorflow import keras
# from tensorflow.keras import Sequential
# from tensorflow.keras.layers import Dense,Flatten
# import matplotlib.pyplot as plt
# from tensorflow.python.keras.metrics import activations
# (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
# # plt.imshow(x_train[2314])
# # plt.show()
# x_train=x_train/255
# x_test=x_test/255

# model=Sequential()
# model.add(Flatten(input_shape=(28,28)))
# model.add(Dense(128,activation='relu'))
# model.add(Dense(10,activation='softmax'))

# model.compile(loss='sparse_categorical_crossentropy',optimizer='Adam')
# model.fit(x_train,y_train,epochs=10,validation_split=0.2)
# y_pred=model.predict(x_test)
# y_pred=y_pred.argmax(axis=1)
# from sklearn.metrics import accuracy_score
# print(accuracy_score(y_test,y_pred))
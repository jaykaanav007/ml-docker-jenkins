from keras.models import Sequential 
from keras.layers import Dense,Conv2D,Flatten
from keras.datasets import mnist
from keras.utils import to_categorical
import numpy as np
(X_train,y_train),(X_test,y_test)=mnist.load_data()
print(X_train.shape)
print(X_test.shape)
X_train = X_train.reshape(60000,28,28,1)
X_test = X_test.reshape(10000,28,28,1)
y_train_one_hot = to_categorical(y_train)
y_test_one_hot = to_categorical(y_test)
model=Sequential()
model.add(Conv2D(64,kernel_size=3,activation='relu',input_shape=(28,28,1)))
model.add(Conv2D(32,kernel_size=3,activation='relu'))
model.add(Flatten())
model.add(Dense(10,activation='softmax'))
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
hist=model.fit(X_train,y_train_one_hot,validation_data=(X_test,y_test_one_hot),epochs=3)
predictions = model.predict(X_test[:10])
print(np.argmax(predictions,axis=1))
print(y_test[:10])

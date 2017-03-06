import sys
sys.path.append('/usr/local/lib/python3.5/dist-packages')
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D
from keras.layers import Activation, Dropout, Flatten, Dense
import numpy as np

# カテゴリの指定
categories = ["chair","camera","butterfly","elephant","flamingo"]
nb_classes = len(categories)
# 画像サイズを指定
image_w = 64
image_h = 64

# データをロード --- (※1)
X_train, X_test, y_train, y_test = np.load("./image/5obj.npy")
# データを正規化する
X_train = X_train.astype("float") / 256
X_test  = X_test.astype("float")  / 256
print('X_train shape:', X_train.shape)

# モデルを構築 --- (※2)
model = Sequential()
model.add(Convolution2D(32, 3, 3,
    border_mode='same',
    input_shape=X_train.shape[1:])) # ----(*2a)
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(64, 3, 3, border_mode='same'))
model.add(Activation('relu'))
model.add(Convolution2D(64, 3, 3))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten()) # --- (※3)
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_classes)) # ---- (*3a)
model.add(Activation('softmax'))

model.compile(loss='binary_crossentropy',
    optimizer='rmsprop',
    metrics=['accuracy'])

# モデルを訓練する --- (※4)
model.fit(X_train, y_train, batch_size=32, nb_epoch=50)

# モデルを評価する --- (※5)
score = model.evaluate(X_test, y_test)
print('loss=', score[0])
print('accuracy=', score[1])

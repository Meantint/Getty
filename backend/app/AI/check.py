import glob
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import load_model


class_names = ['건강보험료납부확인서', '근로소득원천징수', '자동차등록증',
               '자동차등록원부', '자격득실확인서', '자동차매매계약서', '소득금액증명서']

def validation(url):

    model = load_model('.//AI//model_save.h5')
    data = np.array([plt.imread(url, 0)])
    data = np.asarray(data)

    paths = glob.glob('.//datas/*/*.png')
    paths = np.random.permutation(paths)
    print(url)
    print('result is', class_names[np.argmax(model.predict(data))])
    return(class_names[np.argmax(model.predict(data))])
def modelFit():
    paths = glob.glob('.//datas/*/*.png')
    paths = np.random.permutation(paths)

    A = np.array([plt.imread(paths[i], 0) for i in range(len(paths))])
    B = np.array([paths[i].split('/')[-2] for i in range(len(paths))])

    B = pd.get_dummies(B)


    # 모델을 완성합니다.
    X = tf.keras.layers.Input(shape=[256, 256, 3])

    H = tf.keras.layers.Conv2D(6, kernel_size=5, padding='same', activation='relu')(X)
    H = tf.keras.layers.MaxPool2D()(H)

    H = tf.keras.layers.Conv2D(16, kernel_size=5, activation='relu')(H)
    H = tf.keras.layers.MaxPool2D()(H)

    H = tf.keras.layers.Flatten()(H)
    H = tf.keras.layers.Dense(120, activation='relu')(H)
    H = tf.keras.layers.Dense(84, activation='relu')(H)
    Y = tf.keras.layers.Dense(7, activation='softmax')(H)

    model = tf.keras.models.Model(X, Y)
    model.compile(loss='categorical_crossentropy', metrics=['acc'])
    train_x = np.asarray(A)
    train_y = np.asarray(B)
    model.fit(train_x, train_y, epochs=3)

    model.save('model_save.h5')

if __name__ == '__main__':
    modelFit()
    validation('.//forTest//건강보험료납부확인서1.png')
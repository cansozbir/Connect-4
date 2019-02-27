import os
import keras
from keras.layers import Dense

def save_model(model):
    if not os.path.exists('Data/Model'):
        os.makedirs('Data/Model')
    model_json = model.to_json()
    with open("Data/Model/model.json", "w") as model_file:
        model_file.write(model_json)
    model.save_weights('Data/Model/weights.h5')
    print('Model and weights saved')
    return


def get_model():
    model = keras.Sequential()
    model.add(Dense(42,input_dim=42))
    model.add(keras.layers.BatchNormalization())
    model.add(Dense(64, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(64, activation='relu'))
    model.add(Dense(42, activation='relu'))
    model.add(Dense(3, activation='softmax'))
    model.compile(loss='sparse_categorical_crossentropy', optimizer='nadam', metrics=['accuracy'])
    return model
if __name__ == '__main__':
    save_model(get_model())
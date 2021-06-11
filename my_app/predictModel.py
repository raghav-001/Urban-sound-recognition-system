import numpy as np
import librosa

from tensorflow.keras.models import model_from_json
from tensorflow import keras
import tensorflow as tf

import IPython.display as ipd
import matplotlib.pyplot as plt
import librosa.display

classDict = {0: "Air Conditioner", 1: "Car Horn", 2: "Children Playing", 3: "Dog Bark", 4: "Drilling",
             5: "Engine Idling", 6: "Gun shot", 7: "Jack hammer", 8: "Siren", 9: "Street Music"}


def load_model():
    global model
    # load json and create model
    json_file = open('my_app/static/my_app/savedModel/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights("my_app/static/my_app/savedModel/model.h5")
    # print("Loaded model from disk")


def predict_model(file_name):
    # Here kaiser_fast is a technique used for faster extraction
    X, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
    # We extract mfcc feature from data
    mels = np.mean(librosa.feature.melspectrogram(
        y=X, sr=sample_rate).T, axis=0)
    mels = mels.reshape(1, 16, 8, 1)
    a = model.predict(mels)
    classid = (np.argmax(a))
    className = classDict[classid]
    return className


def figure_model(file_name):
    #filename = 'fold5/100852-0-0-0.wav'
    plt.figure(figsize=(12, 4))
    data, sample_rate = librosa.load(file_name)
    _ = librosa.display.waveplot(data, sr=sample_rate)
    plt.savefig("my_app/static/my_app/images/freq1.png")




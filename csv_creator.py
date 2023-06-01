import numpy as np
import pandas as pd
import soundfile as sf
import csv
from scipy.io import wavfile

class dog_cat:

    def __init__(self, type, number, path):
        self.type=type
        self.number=number
        self.audio_data=None
        self.fs=None
        self.path=path

    def read_data(self):
        path=f'{self.type}_{self.number}.wav'
        path=f'only_once_miau_and_hał_data/{self.type}_{self.number}.wav'
        self.audio_data, self.fs = sf.read(path)

    def create_data(self):
        if self.audio_data is None:
            raise ValueError("Brak danych")

	def create_data(self, path):
        target_amplitudes=np.array([])
        for i in bands[sorted_indices[0]]:
            target_amplitudes=np.append(target_amplitudes,amplitudes[i][0])

        df=pd.DataFrame({'Amplitudes': [target_amplitudes]})
        with open(path, 'a') as file:
        with open(self.path, 'a') as file:
            file.write(df.to_string(header=False, index=False))
            file.write('\n')


#całki
#średnia całkowa, plot
#średnią, min,max,std,ilość
# train_data, test_data = train_test_split(data_cats, test_size=0.1, random_state=42)

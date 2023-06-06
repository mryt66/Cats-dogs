import numpy as np
import pandas as pd
import soundfile as sf
import csv
from scipy.io import wavfile

class DogCat:
    
    def __init__(self, type, number, path):
        self.type = type
        self.number = number
        self.audio_data = None
        self.fs = None
        self.path = path

    def read_wave(self):
        path2=f'../data/{self.type}_{self.number:02d}.wav'
        if self.type=='Your_file':
            path2='Your_file.wav'
        self.audio_data, self.fs = sf.read(path2)
    
    def create_data(self):
        if self.audio_data is None:
            raise ValueError("No data")
            
        fft = np.fft.fft(self.audio_data)
        amplitudes = np.abs(fft)
        multiplier = len(amplitudes)/1000
        dt = 1/self.fs
        
        freqs = np.fft.fftfreq(len(fft), dt)

        bands = np.array_split(np.arange(len(freqs)), 1000) 
        mean_amplitude = [np.mean(amplitudes[band]) for band in bands] 
        sorted_indices = np.argsort(mean_amplitude)[::-1]
        
        target_amplitudes=np.array([])
        for i in bands[sorted_indices[0]]:
            target_amplitudes=np.append(target_amplitudes,amplitudes[i][0])
        df = pd.DataFrame([target_amplitudes])
        if self.type=='Your_file':
            return df
        df.to_csv(self.path, index=False, header=False, mode='a')  

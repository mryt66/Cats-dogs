import numpy as np
import pandas as pd
import soundfile as sf
import csv
from sklearn.model_selection import train_test_split
from scipy.io import wavfile

class dog_cat:
    
    def __init__(self, type, number, path):
        self.type=type
        self.number=number
        self.audio_data=None
        self.fs=None
        self.path=path
        
    def read_data(self):
        path=f'only_once_miau_and_hał_data/{self.type}_{self.number}.wav'
        self.audio_data, self.fs = sf.read(path)
        
    def create_data(self):
        if self.audio_data is None:
            raise ValueError("Brak danych")

        fft = np.fft.fft(self.audio_data)
        amplitudes = np.abs(fft)
        
        divide_number=1000
        multiplier=len(amplitudes)/divide_number
        dt = 1/self.fs

        freqs = np.fft.fftfreq(len(fft), dt)
        bands = np.array_split(np.arange(len(freqs)), divide_number) 
        mean_amplitude = [np.mean(amplitudes[band]) for band in bands] 
        sorted_indices = np.argsort(mean_amplitude)[::-1]

        target_amplitudes=np.array([])
        for i in bands[sorted_indices[0]]:
            target_amplitudes=np.append(target_amplitudes,amplitudes[i][0])
        df=pd.DataFrame({'Amplitudes': [target_amplitudes]})
        with open(self.path, 'a') as file:
            file.write(df.to_string(header=False, index=False))
            file.write('\n')
    
   
# for iterator in range(11,25):
#     thing=dog_cat('cat',iterator, 'Data_cats.csv')
#     thing.read_data()
#     thing.create_data()




# data_cats=[]
# with open('Data_cats_10.csv', 'r', newline='') as file:
#     reader=csv.reader(file, quoting=csv.QUOTE_NONE)
#     for i in reader:
#         tmp=[]
#         for j in i:
#             if j[0]=='[':
#                 j=j.strip('[')
#             elif j[len(j)-1]==']':
#                 j=j.strip(']')
#             tmp.append(j)
#         data_cats.append(tmp)
# for i in data_cats:
#     print(i)



#co zrobić !!!
#dorobić zabezpieczenie, żeby nie było dwóch tych samych linijek w .csv     
    
    

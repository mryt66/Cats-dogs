import numpy as np
import soundfile as sf
from scipy.io import wavfile


class dog_cat:
    def __init__(self, data):
        self.data=data
        self.audio_data=None
        self.fs=None
        
    def read_data(self):
        self.audio_data, self.fs = sf.read(f'cat_1-00{self.data}.wav')
        
    def create_data(self):
        if self.audio_data is None:
            raise ValueError("Brak danych")
        # Obliczenie transformaty Fouriera
        fft = np.fft.fft(self.audio_data)

        # Obliczenie amplitud widmowych
        amplitudes = np.abs(fft)

        #divide_number to liczba na ile widm chcemy podzielić nasz dźwięk
        divide_number=1000 
        multiplier=len(amplitudes)/divide_number

        # Obliczenie częstotliwości próbkowania
        dt = 1/self.fs

        # Obliczenie wartości częstotliwości odpowiadającej każdemu elementowi w FFT
        freqs = np.fft.fftfreq(len(fft), dt)
        bands = np.array_split(np.arange(len(freqs)), divide_number) 

        #dodanie średnich amplitud do listy mean_ampltiude
        mean_amplitude = [np.mean(amplitudes[band]) for band in bands] 

        #posortowanie ich tak, żeby znaleźć te o najwyższej amplitudzie 
        sorted_indices = np.argsort(mean_amplitude)[::-1]

        target_amplitudes=np.array([])
        for i in bands[sorted_indices[0]]:
            target_amplitudes=np.append(target_amplitudes,amplitudes[i][0])

        #target to jest tablica na której pracujemy i tu są dane o amplitudach z względem (nwm jakim na częstotliwości)
        print(target_amplitudes)

        #zapis do pliku w 1 linijce tablicy target
        with open('Data_cats_10.csv', 'a') as file:
            np.savetxt(file, [target_amplitudes], fmt='%.8f', delimiter=',')
            
#Wczytanie audio
for iterator in range(1,9):
    thing=dog_cat(iterator)
    thing.read_data()
    thing.create_data()
    

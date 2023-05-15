import numpy as np
import soundfile as sf
from scipy.io import wavfile

# Wczytanie pliku audio
audio_data, fs = sf.read('cat_1.wav')

# Obliczenie transformaty Fouriera
fft = np.fft.fft(audio_data)


# Obliczenie amplitud widmowych
amplitudes = np.abs(fft)

# Obliczenie częstotliwości próbkowania
dt = 1/fs

# Obliczenie wartości częstotliwości odpowiadającej każdemu elementowi w FFT
freqs = np.fft.fftfreq(len(fft), dt)
bands = np.array_split(np.arange(len(freqs)), 1000)
#dodanie średnich amplitud do listy mean_ampltiude
mean_amplitude = [np.mean(amplitudes[band]) for band in bands] 
sorted_indices = np.argsort(mean_amplitude)[::-1]
print(sorted_indices) 
#Indeksy z najwyższymi średnimi amplitudami dla 1000 widm,
#czyli warto brać pod uwagę pierwsze n widm zwłaszcza jak są blisko siebie tzn. z rzędu
#w tym przypadku warto wziąć pod uwagę np. widma od 260 do 270 każde widmo to jakieś 30-60 danych w zależnośći od długości dźwięku
#czyli z 40k danych pracujemy tylko na np. 300 danych dla każdego dźwięku co jest chyba dobrą opcją.

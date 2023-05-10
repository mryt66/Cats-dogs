import csv
import librosa

wav_files=[]

#zapis 10 znormalziwoanych danych kotów do pliku csv 
with open('Data_cats_10.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for file in range(1,3):
        path = f'cat_0{file}.wav'
        y, sr = librosa.load(path)
        [e for e in y if abs(e)>0.0001]
        writer.writerow(y) #zapis do pliku

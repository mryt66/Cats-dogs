import csv
import librosa

wav_files=[]

#zapis 10 znormalziwoanych danych kotów do pliku csv 
with open('Data_cats_10.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    for file in range(1,10):
        path = rf'D:\Projekty\SSI_cat_dog\archive\checked_dataset\cat_0{file}.wav'
        y, sr = librosa.load(path)
        writer.writerow(y) #zapis do pliku



import numpy as np
import pandas as pd
import soundfile as sf
import csv
from sklearn.model_selection import train_test_split
from scipy.io import wavfile
from csv_creator.py import dog_cat

csv_cats='Data_cats.csv'
csv_dogs='Data_dogs.csv'

for iterator in range(10,26):
    thing=dog_cat('cat',iterator)
    thing.read_data()
    thing.create_data('Data_cats.csv')
    
    thing=dog_cat('dog_barking',iterator)
    thing.read_data()
    thing.create_data('Data_dogs.csv')

    

data_cats=[]
with open(csv_cats, 'r', newline='') as file:
    reader=csv.reader(file, quoting=csv.QUOTE_NONE)
    for i in reader:
        tmp=[]
        for j in i:
            if j[0]=='[':
                j=j.strip('[')
            elif j[len(j)-1]==']':
                j=j.strip(']')
            tmp.append(j)
        data_cats.append(tmp)
for i in data_cats:
    print(i)

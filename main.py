#A file which should be named main.ipynb but github can't read this extension.

import numpy as np
import pandas as pd
import random
import csv
import os
from statistics import mean
from csv_creator import dog_cat
from load_data import load_data
from classifier import KNN


# Tworzenie danych i zapis do .csv
if os.path.getsize('Data_cats.csv')==0 and os.path.getsize('Data_dogs.csv')==0:
    for i in range(1,26):
        thing=dog_cat('cat', i, 'Data_cats.csv')
        thing.read_wave()
        thing.create_data()

        thing=dog_cat('dog_barking', i, 'Data_dogs.csv')
        thing.read_wave()
        thing.create_data()

# Odczyt z .csv pliku, charakteryzacja danych dla listy
data=[]

def load_csv(file, type):
    with open(file, newline='') as file:
        reader=csv.reader(file, quoting=csv.QUOTE_NONE)
        for i in reader:
            tmp=[]
            for j in i:
                if j[0]=='[':
                    j=j.strip('[')
                elif j[len(j)-1]==']':
                    j=j.strip(']')
                tmp.append(float(j))
            dl=1
            num=0
            for j in tmp:
                dl=dl+1
                num+=float(j)
            if dl>5:
                data.append([mean(tmp), min(tmp), max(tmp), dl-1, type])
    return data

load_csv('Data_cats.csv','cats')
load_csv('Data_dogs.csv','dogs')
    
x=load_data(data)
x.shuffle()
train,val=x.split()

#KNN dla poszczególnej liczby danych
k=5
y=KNN(train,val,k)
y.classify()


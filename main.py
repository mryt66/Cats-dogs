#A file which should be named main.ipynb but github can't read this extension.

import numpy as np
import pandas as pd
import soundfile as sf
import random
import csv
from statistics import mean
from scipy.io import wavfile
from csv_creator import dog_cat

for iterator in range(10,26):
    thing=dog_cat('cat', iterator, 'Data_cats.csv')
    thing.read_wave()
    thing.create_data()
    
    thing=dog_cat('dog_barking', iterator, 'Data_dogs.csv')
    thing.read_wave()
    thing.create_data()

data=[]

def load_csv(file, type):
    with open(file, newline='') as file:
        reader=csv.reader(file, quoting=csv.QUOTE_NONE)
        for i in reader:
            tmp=[]
            for j in i:
                if j[0]=='[':
                    j=float(j.strip('['))
                elif j[len(j)-1]==']':
                    j=float(j.strip(']'))
                else:
                    j=float(j)
                tmp.append(j)
            
            dl=1
            num=0
            for j in tmp:
                dl=dl+1
                num+=float(j)
            if dl>5:
                data.append([mean(tmp), type, dl-1, min(tmp), max(tmp)])
    return data

load_csv('Data_cats.csv','cats')
load_csv('Data_dogs.csv','dogs')

class load_data:
    
    def __init__(self, data):
        self.data=data
        
    def shuffle(self):
        for i in range(len(self.data) - 1, 0, -1):
            j = random.randint(0, i)
            self.data[i], self.data[j] =  self.data[j], self.data[i]
        return self.data
    
    def split(self):
        split=int(len(self.data)*0.9)
        listTrain = self.data[0:split]
        listVal = self.data[split: len(self.data)]
        return listTrain, listVal
       
x=load_data(data)
x.shuffle()
train,val=x.split()
k=3
print(train)


    

    

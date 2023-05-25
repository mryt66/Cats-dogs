import numpy as np
import pandas as pd
import soundfile as sf
import csv
from sklearn.model_selection import train_test_split
from scipy.io import wavfile

data_cats=[]
with open('Data_cats_10.csv', 'r', newline='') as file:
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

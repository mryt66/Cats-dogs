#A file which should be named main.ipynb but github can't read this extension.

import numpy as np
import pandas as pd
import soundfile as sf
import csv
from sklearn.model_selection import train_test_split
from scipy.io import wavfile
from csv_creator import dog_cat


for iterator in range(10,26):
    thing=dog_cat('cat',iterator,'Data_cats.csv')
    thing.read_data()
    thing.create_data()
    
    thing=dog_cat('dog_barking',iterator,'Data_dogs.csv')
    thing.read_data()
    thing.create_data()

    
#odczytywanie z pliku

# data_cats=[]
# with open(csv_cats, 'r', newline='') as file:
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
    
    
##ZMIANY
import numpy as np
import pandas as pd
import soundfile as sf
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import csv
from sklearn.model_selection import train_test_split
from scipy.io import wavfile

data_cats=[]
data_dogs=[]

with open('Data_cats.csv', newline='') as file:
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

with open('Data_dogs.csv', newline='') as file:
    reader=csv.reader(file, quoting=csv.QUOTE_NONE)
    for i in reader:
        tmp=[]
        for j in i:
            if j[0]=='[':
                j=j.strip('[')
            elif j[len(j)-1]==']':
                j=j.strip(']')
            tmp.append(j)
        data_dogs.append(tmp)

#nie wiem czy to nie musi być w 1 data secie z odpowiednimi etykietami
train_cats, test_cats = train_test_split(data_cats, test_size=0.1, random_state=42)
train_dogs, test_dogs = train_test_split(data_cats, test_size=0.1, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(train_cats)
X_test_scaled = scaler.transform(X_test)


knn = KNeighborsClassifier(n_neighbors=5)
test_dogs[0]

    

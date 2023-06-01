import numpy as np
import pandas as pd
import soundfile as sf
import random
from statistics import mean
from scipy.io import wavfile

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

#całki
#średnia całkowa, plot
#średnią, min,max,std,ilość

# train_data, test_data = train_test_split(data_cats, test_size=0.1, random_state=42)

# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(train_cats)
# X_test_scaled = scaler.transform(X_test)

# knn = KNeighborsClassifier(n_neighbors=5)

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

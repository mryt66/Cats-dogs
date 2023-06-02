import random


class load_data:
    def __init__(self, data):
        self.data=data
        
    def shuffle(self):
        for i in range(len(self.data) - 1, 0, -1):
            j = random.randint(0, i)
            self.data[i], self.data[j] =  self.data[j], self.data[i]
        return self.data
    
    def split(self):
        split=int(len(self.data)*0.5)
        listTrain = self.data[0:split]
        listVal = self.data[split: len(self.data)]
        return listTrain, listVal
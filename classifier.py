import numpy as np

class KNN:
    def __init__(self, train, val, k):
        self.train=train
        self.val=val
        self.k=k
    
    def euclidean_dist(self, x1, x2):
        x1=np.array(x1[:-1])
        x2=np.array(x2[:-1])
        return np.sqrt(np.sum((x1 - x2)**2))
    
    def classify(self):
        properly_estimated=0
        tmp1=[]
        for i in self.val:
            tmp2=[]
            for j in self.train:
                tmp2.append([self.euclidean_dist(i,j),j[4]]) 
            tmp2.sort()
            tmp1.append(tmp2)
        
        for i in range(len(tmp1)):
            cats=0
            dogs=0
            for j in range(0,self.k):
                if tmp1[i][j][1]=='cats':
                    cats+=1
                else:
                    dogs+=1
            if cats>dogs and self.val[i][4]=='cats':
                properly_estimated+=1
            elif dogs>cats and self.val[i][4]=='dogs':
                properly_estimated+=1
                
        print("Skuteczność klasyfikatora wynosi około",round((properly_estimated/len(tmp1)*100),2),'%')
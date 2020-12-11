# -*- coding: utf-8 -*-
"""
Created on Fri Aug  2 20:15:44 2019

@author: andok
"""
from generator import generateName
import random as rd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import numpy as np


print("\n##Name factory")

session = input("Choose session name : " )
basefile = input("Choose base names file : " )

names = extractNames(basefile)
flfreq = computeFirstLetterFreq(names)  
mat =  computeTransMat(names)

file_names = open("generated/"+session+"_names.txt","w")

number = int(input("How many names? "))
generated_names = []
for i in range(number) :
    name, seq =  generateName(mat, flfreq);
    file_names.write(name)
    generated_names.append(name)
    

file_names.close()
file_seq.close()

#%%



real_names_file = open(basefile , "r")

real_names = real_names_file.readlines()
n_real = len(real_names)

generated_train_names =  generated_names[:min(number//5, 300)]
n_generated = len(generated_train_names)

test_names = generated_names[min(number//5, 300):]
real_names_file.close()


train_names = real_names + generated_train_names

X_train = []
for nm in train_names :
    X_train.append(nameToVect(nm))
    
dim = len(X_train[0])

X_test = []
for nm in test_names :
    X_test.append(nameToVect(nm))
    
    
y_train = [1]*len(real_names) + [0]*len(generated_train_names) 

N = len(X_train)
indices = list(range(N))
rd.shuffle(indices)
X_train = np.array(X_train).reshape((N,dim))
X_test = np.array(X_test).reshape((len(test_names),dim))
y_train = np.array(y_train)
X_train = X_train[indices]
y_train = np.array(y_train[indices], dtype =np.float32)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)
#%%
neigh = KNeighborsClassifier(n_neighbors=5)
neigh.fit(X_train, y_train)
y_pred = neigh.predict(X_test)
good_names = [test_names[i] for i in np.where(y_pred == 1)[0].tolist()]
good_names =list(set(good_names))
good_names.sort()
file_gn = open("generated/"+session+"_good_names_knn.txt", "w")
for nm in good_names :
    file_gn.write(nm)
file_gn.close()



#%%
forest = RandomForestClassifier(n_estimators =10)
forest.fit(X_train, y_train)
y_pred = forest.predict(X_test)
good_names = [test_names[i] for i in np.where(y_pred == 1)[0].tolist()]
good_names =list(set(good_names))
good_names.sort()
file_gn = open("generated/"+session+"_good_names_forest.txt", "w")
for nm in good_names :
    file_gn.write(nm)
file_gn.close()

print("Done")



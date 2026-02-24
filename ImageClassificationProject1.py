#Image Classification (using Random Forrest Classifier Algorithm)
#Working with MNIST dataset (downloaded from Kaggle); it is a real-time dataset of handwritten digits.
#done in VS Code

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import time

#using pandas to read the msint dataset
data = pd.read_csv('mnist_test.csv')
#viewing column head
#print(data.head())

'''extracting the particular image (pixel data) from the itneger location  of 4th row (3rd index) 
and collecting columns 1 to the end (not 0, because it is the label of the image there).'''
# a = data.iloc[100,1:].values      
# #reshaping the extracted pixel into workable size
# a = a.reshape(28,28).astype('uint8')
# plt.imshow(a, interpolation='nearest')
# plt.show()

'''preparing the data by separting labels and its values'''
x= data.iloc[:,1:]
y = data.iloc[:,0]

''' creating test and train batches'''
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=4)
#checking
# print(x_train.head())
# print(y_train.head())

'''calling RandomForestClassifier'''
rf = RandomForestClassifier(n_estimators=100)
'''fitting the model'''
start_time = time.time()
rf.fit(x_train,y_train)

end_time = time.time()
print(f"Fitting done in {end_time - start_time:.2f}s")

#prediction on test data
pred = rf.predict(x_test)
print("Prediction is:",pred)
#checking accuracy
test = y_test.values
#calculating no. of correct prediction
count=0
for i in range(len(pred)):
    if pred[i]==test[i]:
        count+=1
print("No. of correct predictions:",count,"out of",len(pred))
print(f"Accuracy Percentage: {(count/len(pred)*100):.2f}%")
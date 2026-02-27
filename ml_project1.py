'''Iris Flower dataset : The dataset contains a set of 150 records under 5 attributes - 
Petal Length, Petal Width, Sepal Length, Sepal width and Class(Species).
It is part of the sklearn library.'''

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn import datasets

'''loading the dataset'''
data = datasets.load_iris()    #loads and return the iris classification dataset

# print(data.keys())      #gives the meta-data of this dataset
# print(data["feature_names"])    #gives the featres on which the data is classified, petal/sepal - lenght/width
# print(data['data'][:5])     #retrieves 5 of the actual records corresponding to each feature
# print(data["target_names"])  # the classes of the iris flower present (3: 0,1,2)
# print(data["target"])       #gives an array of value of corresponding class

'''motive of project: 
trying to predict the species of iris flower based on its attributes using the feutures given here.
this is a multiclass classification probelm.'''

#working with the data using pandas aand numpy


df = pd.DataFrame(data['data'], columns=data['feature_names'])
df["target"] = data['target']

#print(df.head())       #gives first 5 records from the dataset
#print(df.describe())   #gives meta-data of the data from the dataset (the min val., max val., count, etc)

# col = "sepal length (cm)"
# df[col].hist()                  #gives the histogram of a pandas series (a column of a pandas dataframe)
# plt.suptitle(col)               #gives the column name as the (super) title of the visual distributuion
# plt.show()                     #gives the output visual distributuion

# col = "sepal width (cm)"
# df[col].hist()                  
# plt.suptitle(col)               
# plt.show() 

# col = "petal length (cm)"
# df[col].hist()                  
# plt.suptitle(col)               
# plt.show()

# col = "petal width (cm)"
# df[col].hist()                  
# plt.suptitle(col)               
# plt.show()


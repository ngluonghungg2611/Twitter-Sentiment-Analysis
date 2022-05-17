import numpy as np
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import warnings
train = pd.read_csv('Train.csv')
test = pd.read_csv('Test.csv')
print("Shape of train set:", train.shape)
print("Shape of test set:", test.shape)

print("-----------------------------")

train['len_text'] = train['text'].str.len()
test['len_text'] = test['text'].str.len()
# print(train)

67
print(cols)
print(train.info())
import numpy as np
import pandas as pd

df = pd.read_csv('input.txt',columns = ['Damage']) # I have removed the first element 1000000 to make manipulation of data easier
print df.describe()   #helps to know the distribution of data mean 4.99 max 9 as well as 1-3 , 3-5,5-7 and 7-9 have equal no. of observations
health = 2000
max_injuries = 1000000
count = 0
injuries = 1
#Since distribution of 1-3 3-5 5-7 and 7-9 is same we first check if we can iterate over all 1-3 , 3-5 elements so that we maximize our count while minimizing the damage and then check for greater 
while (health > 1 and max_injuries < 1000000): 
	for index, row in df.iterrows():
		if(row['Damage']<= 5)
			health = health - row['Damage']
			injuries = injuries * row['Damage']
			count += 1
while (health > 1 and max_injuries < 1000000): 
	for index, row in df.iterrows():
		if(row['Damage']> 5)
			health = health - row['Damage']
			injuries = injuries * row['Damage']
			count += 1
print count

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
dataset = pd.read_csv(r'C:\Users\Ishan Ambasta\Desktop\Artefact\Abhinav\Arimax_v3_wo_covid_Swapnil.csv')


x=dataset[['Year','Month','marketingSpend']]
y=dataset[['Visitors']]

#Splitting Training and Test Set
#Since we have a very small dataset, we will train our model with all availabe data.

from sklearn.ensemble import RandomForestRegressor
regressor = RandomForestRegressor(n_estimators=100,max_depth=2, random_state=5)

#Fitting model with trainig data
regressor.fit(x, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[2020,1,20000]]))



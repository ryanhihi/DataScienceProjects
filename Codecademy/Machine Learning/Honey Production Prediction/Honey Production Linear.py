
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("honeyproduction.csv")

#Investigate data structure:
print(df.head())

#Total production of honey per year:
prod_per_year = df.groupby('year').totalprod.mean().reset_index()
#print(prod_per_year.head())

#Year as X variable and reshaspe:
X = prod_per_year['year'].values.reshape(-1,1)

#Set totalprod as Y
y = prod_per_year['totalprod']

#Plot X and y
plt.scatter(X,y)
plt.show()

#Create linearRegression Model
regr = linear_model.LinearRegression()
#Fit the model to X and y:
regr.fit(X, y)

#Print the slope and intercept:
print(regr.coef_[0])
print(regr.intercept_)

#Predictions of the model:
y_predict = regr.predict(X)

#Plot the Predictions and X:
plt.scatter(X, y_predict)
plt.scatter(X,y)
plt.show()

#Prediction for year 2050
#Create X future nums from year 2013 to 2050:
X_future = np.array(range(2013,2051))
X_future = X_future.reshape(-1,1)
#Future prediction:
future_predict = regr.predict(X_future)
#Plot :
plt.scatter(X_future, future_predict)
plt.scatter(X,y)
plt.show()
print(future_predict[-1])

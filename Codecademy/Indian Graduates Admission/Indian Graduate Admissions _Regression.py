import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import accuracy_score
import numpy as np
from sklearn import tree
import matplotlib.pyplot as plt

df = pd.read_csv("Admission_Predict.csv")
df.columns = df.columns.str.strip().str.replace(' ','_').str.lower()

#e will use the unaltered chance_of_admit target,
# which is a floating point value between 0 and 1
X = df.loc[:,'gre_score':'research']
y = df['chance_of_admit']

#using DecisionTreeRegressor:
x_train, x_test, y_train, y_test = train_test_split(X,y, random_state=0, test_size=0.2)
dt = DecisionTreeRegressor(max_depth=3, ccp_alpha=0.001)
dt.fit(x_train, y_train)
y_pred = dt.predict(x_test)
print(dt.score(x_test, y_test))

#Visualize the tree
plt.figure(figsize=(10,10))
tree.plot_tree(dt, feature_names = x_train.columns,
               max_depth=2, filled=True);
plt.show()
plt.clf()

#Split Criteria
#Calculate the Mean Squared ErrorInstead of the Gini Impurity
def mse(data):
    """Calculate the MSE of a data set
    """
    return np.mean((data - data.mean()) ** 2)


def mse_gain(left, right, current_mse):
    """Information Gain (MSE) associated with creating a node/split data based on MSE.
    Input: left, right are data in left branch, right banch, respectively
    current_impurity is the data impurity before splitting into left, right branches
    """
    # weight for gini score of the left branch
    w = float(len(left)) / (len(left) + len(right))
    return current_mse - w * mse(left) - (1 - w) * mse(right)


m = mse(y_train)
print(f'MSE at root: {round(m, 3)}')

mse_gain_list = []
for i in x_train.cgpa.unique():
    left = y_train[x_train.cgpa <= i]
    right = y_train[x_train.cgpa > i]
    mse_gain_list.append([i, mse_gain(left, right, m)])

mse_table = pd.DataFrame(mse_gain_list, columns=['split_value', 'info_gain']).sort_values('info_gain', ascending=False)
print(mse_table.head(10))

#Visulize the information gained
plt.plot(mse_table['split_value'], mse_table['info_gain'],'o')
plt.plot(mse_table['split_value'].iloc[0], mse_table['info_gain'].iloc[0],'r*')
plt.xlabel('cgpa split value')
plt.ylabel('info gain')
plt.show()
plt.clf()

print(np.unique(dt.predict(x_train)))
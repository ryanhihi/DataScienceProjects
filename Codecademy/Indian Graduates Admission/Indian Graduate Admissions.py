import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt

df = pd.read_csv("Admission_Predict.csv")
df.columns = df.columns.str.strip().str.replace(' ','_').str.lower()

#As a first step, we will create a binary class (1=admission likely , 0=admission unlikely) from the chance of admit –
# greater than 80% we will consider as likely.
#The remaining data columns will be used as predictors.

X = df.loc[:,'gre_score':'research']
y = df['chance_of_admit']>=.8

#Using Decision Tree
#Fitting and Predicting
x_train, x_test, y_train, y_test = train_test_split(X,y, random_state=0, test_size=0.2)
dt = DecisionTreeClassifier(max_depth=2, ccp_alpha=0.01,criterion='gini')
dt.fit(x_train, y_train)
y_pred = dt.predict(x_test)
print(dt.score(x_test, y_test))
print(accuracy_score(y_test, y_pred))

#Visualize the Decision Tree
tree.plot_tree(dt, feature_names = x_train.columns,
               max_depth=3, class_names = ['unlikely admit', 'likely admit'],
               label='root', filled=True)
plt.show()
plt.clf()
print(tree.export_text(dt, feature_names = X.columns.tolist()))

# Split Criteria
#Determine how the tree was splitted
#Our tree has already been built for us, but how was the split cgpa<=8.845 determined

#WE calculate gini and information gained
#Gini Impurities
def gini(data):
    """Calculate the Gini Impurity Score
    """
    data = pd.Series(data)
    return 1 - sum(data.value_counts(normalize=True) ** 2)


gi = gini(y_train)
print(f'Gini impurity at root: {round(gi, 3)}')

#information gained
def info_gain(left, right, current_impurity):
    """Information Gain associated with creating a node/split data.
    Input: left, right are data in left branch, right banch, respectively
    current_impurity is the data impurity before splitting into left, right branches
    """
    # weight for gini score of the left branch
    w = float(len(left)) / (len(left) + len(right))
    return current_impurity - w * gini(left) - (1 - w) * gini(right)

#determine how e split on cgpa was determined
#cgpa is a continuous variable, which adds an extra complication, as the split can occur for ANY value of cgpa
#We will use info_gain over ALL values of cgpa to determine the information gain when split on each value.
# This is stored in a table and sorted, and voila, the top value for the split is cgpa<=8.845!
# This is also done for every other feature (and for those continuous ones, every value), to find the top split overall.
info_gain_list = []
for i in x_train.cgpa.unique():
    left = y_train[x_train.cgpa<=i]
    right = y_train[x_train.cgpa>i]
    info_gain_list.append([i, info_gain(left, right, gi)])

ig_table = pd.DataFrame(info_gain_list, columns=['split_value', 'info_gain']).sort_values('info_gain',ascending=False)
print(ig_table.head(10))

plt.plot(ig_table['split_value'], ig_table['info_gain'],'o')
plt.plot(ig_table['split_value'].iloc[0], ig_table['info_gain'].iloc[0],'r*')
plt.xlabel('cgpa split value')
plt.ylabel('info gain')
plt.show()
plt.clf()

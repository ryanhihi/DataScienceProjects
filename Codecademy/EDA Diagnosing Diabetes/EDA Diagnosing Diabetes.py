import pandas as pd
import numpy as np

diabetes_data = pd.read_csv('diabetes.csv')
print(diabetes_data.head(10))
#Invest the dataframe to see how many columns and rows
print(diabetes_data.info())

#Inspect how many columns contain null
print(diabetes_data.isnull().sum())

#Investigate further
print(diabetes_data.describe())
#
#Looking at the summary statistics,
#Glucose
#BloodPressure
#SkinThickness
#Insulin
#BMI
#The minimum value for all 5 columns are all 0
#THERE are outliers in the data where Insulin = 846 and Pregnancies =17 which are impossibles

#Data cleaning performing
#Replace 0 with NaN in the five columns mentioned above

diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']].replace(0, np.nan)
#Check the number of Null entry again
print(diabetes_data.isnull().sum())

#Investigate why some data might be missing
print(diabetes_data[diabetes_data.isnull().any(axis=1)])

#Determine the type of missing
#  rows with missing data have missing values in more than one column.
#  In fact, every single row with at least one missing value also has a missing value in the insulin column
# The pattern also happens most isulin misssing associated with skin thickness missing

print(diabetes_data.dtypes)

#It looks like the Outcome column is of type object (string) even though in our initial inspection we expected it to be of type int64
print(diabetes_data.Outcome.unique())
#Need to replace '0' with 0 and convert type into string
diabetes_data['Outcome'] = diabetes_data['Outcome'].replace('O', 0)
diabetes_data['Outcome'] = diabetes_data['Outcome'].replace('0', 0)
print(diabetes_data['Outcome'].unique())
diabetes_data['Outcome'] =diabetes_data['Outcome'].astype(int)
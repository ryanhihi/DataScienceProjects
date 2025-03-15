import pandas as pd
import numpy as np

#load the csv file for initial approach to the dataset
recipes = pd.read_csv('recipe_site_traffic_2212.csv')

#print(recipes)
#investigate the missing values
print('Missing values:')
print(recipes.isnull().any())

#check the data type:
print('Data Type:')
print(recipes.dtypes)
#only servings data type doesntmeet the description as numeric

# Missing values in [calories, carbohydrate, sugar, protein, high_traffic] columns.

#Count missing values
print(recipes.isnull().sum().sum())
#total 581 missing values in the dataset

#calories
print(recipes['calories'].isnull().sum()) #52 missing values
#data type is correct

#carbohydrate
print(recipes['carbohydrate'].isnull().sum())# 52 missing values
#data type is correct

#sugar
print(recipes['sugar'].isnull().sum())# 52 missing values
#data type is correct

#protein
print(recipes['protein'].isnull().sum())# 52 missing values
#data type is correct

#category
print(recipes['category'].isnull().sum())# 0 missing values
#data type is correct
#count number of unique values in column
print(recipes['category'].nunique()) # 11 unique values, should be 10
print(recipes['category'].unique()) #print all the unique values
# check how many of the data were categorized as "Chicken Breast"
print((recipes['category']== 'Chicken Breast').sum()) # 98 recipes was labeled as "Chicken Breast" should be replaced to "Chicken"

recipes['category'] = recipes['category'].replace('Chicken Breast', 'Chicken')
print(recipes['category'].nunique()) # 11 unique values, should be 10
print(recipes['category'].unique()) #print all the unique values

#servings
print(recipes['servings'].unique()) #print all the unique values
recipes['servings'] = recipes['servings'].str.extract('(\d+)')[0]
recipes['servings'] = pd.to_numeric(recipes['servings'], errors = 'coerce')
print(recipes['servings'].unique()) #print all the unique values

#high_traffic:
print(recipes['high_traffic'].isnull().sum())# 373 missing values
print(recipes['high_traffic'].unique()) #print all the unique values
#replace nan with "Low"
recipes['high_traffic'] = recipes['high_traffic'].fillna('Low')
print(recipes['high_traffic'].unique()) #print all the unique values

# REmove all missing data
cleaned_recipes = recipes.dropna()

print(cleaned_recipes)

#Save to the new csv
cleaned_recipes.to_csv('cleaned_recipes.csv', index=False)
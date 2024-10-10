# Import pandas with alias
import pandas as pd

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)
#The census dataframe is composed of simulated census data to represent demographics of a small community in the U.S. Call the .head() method on the census dataframe and print the output to view the first five rows.
print(census.head(5))

#Review the dataframe description and values returned by .head() to assess the variable types of each of the variables. This is an important step to understand what preprocessing will be necessary to work with the data.
print(census.dtypes)
#Compare the values returned from the .head() method with the data types of each variable by calling .dtypes on the census dataframe and print the result.
print(census.info())

#The manager of the census would like to know the average birth year of the respondents. We were able to see from .dtypes that birth_year has been assigned the str datatype whereas it should be expressed in int.
#Print the unique values of the variable using the .unique() method.
#There appears to be a missing value in the birth_year column. With some research you find that the respondent’s birth year is 1967.
#Use the .replace() method to replace the missing value with 1967, so that the data type can be changed to int. Then recheck the values in birth_year by calling the .unique() method and printing the results.
census['birth_year'] = census['birth_year'].replace(['missing'], 1967)
print(census.birth_year.unique())
census['birth_year'] = census['birth_year'].astype(int)
print(census.dtypes)
print(census.birth_year.mean())

#Your manager would like to set an order to the higher_tax variable so that: strongly disagree < disagree < neutral < agree < strongly agree.
#Convert the higher_tax variable to the category data type with the appropriate order, then print the new order using the .unique() method.
census.higher_tax=pd.Categorical(census.higher_tax,['strongly disagree','disagree','neutral','agree','strongly agree'], ordered=True)
print(census.higher_tax.unique())

#Your manager would also like to know the median sentiment of the respondents on the issue of higher taxes for the wealthy. Label encode the higher_tax variable and print the median using the pandas .median() method.
census.higher_tax = census.higher_tax.cat.codes
print(census.higher_tax.median())

#Your manager is interested in using machine learning models on the census data in the future. To help, let’s One-Hot Encode marital_status to create binary variables of each category. Use the pandas get_dummies() method to One-Hot Encode the marital_status variable.
#Print the first five rows of the new dataframe with the .head() method. Note that you’ll have to scroll to the right or expand the web-browser to see the dummy variables.
census = pd.get_dummies( data = census, columns = ['marital_status'])
print(census.head(5))
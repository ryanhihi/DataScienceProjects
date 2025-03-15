import pandas as pd
pd.set_option('display.max_colwidth', -1)

#Write a function that filters the dataset for questions that contains all of the words in a list of words. For example, when the list ["King", "England"] was passed to our function, the function returned a DataFrame of 152 rows. Every row had the strings "King" and "England" somewhere in its " Question".

#Note that in this example, we found 152 rows by filtering the entire dataset. You can download the entire dataset at the start or end of this project. The dataset used on Codecademy is only a fraction of the dataset so you won’t find as many rows.

#Test your function by printing out the column containing the question of each row of the dataset.
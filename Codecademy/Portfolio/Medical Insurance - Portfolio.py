import csv
with open("insurance.csv") as insurance:
    insurance_data = list(csv.reader(insurance, delimiter=','))
    # for line in insurance_data:
    #     print(line)

#Analysis

#function to calculate average insurance charges:
def average_charges(insurance_data):
    total_charges = 0
    for row in insurance_data[1:]:
        total_charges += float(row[6])
    return total_charges/(len(insurance_data)-1)

#function to find max and min
def find_max_min_insurance_costs(insurance_data):
    # Initialize variables to store max and min insurance costs
    max_cost = float('-inf')  # Initialize max_cost to negative infinity
    min_cost = float('inf')   # Initialize min_cost to positive infinity

    # Iterate through the insurance data
    for row in insurance_data[1:]:
        cost = float(row[6])  # Assuming 'charges' is in the 7th column
        # Update max and min values if necessary
        if cost > max_cost:
            max_cost = cost
        if cost < min_cost:
            min_cost = cost

    # Return the maximum and minimum insurance costs
    return max_cost, min_cost


#Detemine the Distribution of data set
#Average insurance charge of total population:
average_charge_all = average_charges(insurance_data)
print(average_charge_all)
#Range by max and min of the total population:
max_cost, min_cost = find_max_min_insurance_costs(insurance_data)
print("Maximum insurance cost:", max_cost)
print("Minimum insurance cost:", min_cost)


#Determine the distribution of dataset based on gender:
total_male = 0
total_female = 0
for row in insurance_data[1:]:
    if row[1] == "male":
        total_male += 1
    if row[1] == "female":
        total_female += 1
print("Total Male: ",total_male)
print("Total Female: ",total_female)
print("Percentage of male/female are: ",(total_male/(len(insurance_data)-1))*100, " percent and ", (total_female/(len(insurance_data)-1))*100, " percent")

male_candidate = []
female_candidate = []
for row in insurance_data[1:]:
    if row[1] == "male":
        male_candidate.append(row)
    if row[1] == "female":
        female_candidate.append(row)

#Calculate the  average insurance cost by gender
#Male
average_male = average_charges(male_candidate)
print("Average Male: ",average_male)

#Female
average_female = average_charges(female_candidate)
print("Average Female: ",average_female)

#Calculate teh average insurance cost by smoker& non-Smoker
smoker = []
non_smoker = []

for row in insurance_data[1:]:
    if row[4] == "yes":
        smoker.append(row)
    if row[4] == "no":
        non_smoker.append(row)

average_smoker = average_charges(smoker)
average_non_smoker = average_charges(non_smoker)

print("Average Smoker: ", average_smoker)
print("Average Non-Smoker: ", average_non_smoker)

import numpy as np
import pandas as pd 
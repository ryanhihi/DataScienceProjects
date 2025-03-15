#Storing patient names and insurance costs
medical_cost = {}

medical_cost['Marina'] = 6607.0
medical_cost['Vinay'] = 3225.0

medical_cost.update({"Connie":8886.0, "Isaac":16444.0, "Valentina":6420.0})

print(medical_cost)

medical_cost['Vinay'] = 3325.0
print(medical_cost)

#Calculate the average medical cost:
total_cost = 0
for value in medical_cost.values():
    total_cost += value

average_cost = total_cost/len(medical_cost)
print("Average Insurance Cost:", average_cost)

#List Comprehension to Dictionary
names = ['Marina', 'Vinay', 'Connie', 'Isaac', 'Valentina']
ages = [27, 24, 43, 35, 52]

zipped_ages = zip(names, ages)

names_to_ages = {key: value for key, value in zipped_ages}
print(names_to_ages)

marina_age = names_to_ages.get('Marina', None)
print(marina_age)

#Using a Dictionary to create a medical database
medical_records = {}
medical_records['Marina'] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 25.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records["Isaac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}
print(medical_records)
print("Connie's insurance cost is ", medical_records["Connie"]["Insurance_cost"], " dollars.")
medical_records.pop("Vinay", None)

for key, value in medical_records.items():
    print(key, " is a ", str(value["Age"]), " year old ", value["Sex"], value["Smoker"], "\n", "with a BMI of ", str(value["BMI"]), " and insurance cost of ", str(value["Insurance_cost"]))
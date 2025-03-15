medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

#print(medical_data)
#Replace # sign with $ for insurance costs
updated_medical_data = medical_data.replace('#', '$')
print(updated_medical_data)

#Calculate the number of records in data
num_records = 0;
for character in updated_medical_data:
    if character == '$':
        num_records += 1

print("There are {} medical records in the database".format(num_records))

#Clean up the data
#Spliting the updated_medical_data string into a list of medical records
medical_data_split = updated_medical_data.split(';')
print(medical_data_split)
#split each medical record into its own list
medical_records = []
for record in medical_data_split:
    medical_records.append(record.split(','))

print(medical_records)

#Removing white space:
medical_records_clean = []
for record in medical_records:
    record_clean = []
    for item in record:
        record_clean.append(item.strip())
    medical_records_clean.append(record_clean)

print(medical_records_clean)


#Analyze Data
#print the name of individuals

for record in medical_records_clean:
    print(record[0])

#Print all the names uppercase
for record in medical_records_clean:
    print(record[0].upper())

names = []
ages = []
bmis = []
insurance_costs = []

for record in medical_records_clean:
    names.append(record[0])
    ages.append(record[1])
    bmis.append(record[2])
    insurance_costs.append(record[3])

print(names)
print(ages)
print(bmis)
print(insurance_costs)
#Calculate average BMI
total_bmi = 0
for bmi in bmis:
    total_bmi += float(bmi)

average_bmi = total_bmi/len(bmis)
print("Average BMI: {}".format(average_bmi))

#Calculate average costs:
total_cost = 0
for cost in insurance_costs:
    total_cost += float(cost.strip('$'))

average_cost = total_cost/len(insurance_costs)
print(total_cost)
print("Average Insurance Cost: {}".format(average_cost))
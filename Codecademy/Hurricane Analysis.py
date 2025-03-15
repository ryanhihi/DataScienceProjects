# names of hurricanes
from collections import defaultdict

names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}
def update(damages):
    update_damages = []
    for damage in damages:
        if damage == "Damages not recorded":
            update_damages.append(damage)
        else:
            numerate_part = float(damage[:-1])
            unit = damage[-1]
            if unit in conversion:
                update_damages.append((numerate_part * conversion[unit]))
            else:
                update_damages.append(damage)
    return update_damages
# test function by updating damages

update_damages = update(damages)
print(update_damages)


# 2
# Create a Table
def construc_dictionary(names,months, years, max_sustained_winds, areas_affected, damages, deaths):
    dictionary = {}
    for i in range(len(names)):
        dictionary[names[i]] = {
            "Name" : names[i],
            "Month" : months[i],
            "Year" : years[i],
            "Max Sustained Winds" : max_sustained_winds[i],
            "Area Affected" : areas_affected[i],
            "Damage" : damages[i],
            "Death" : deaths[i]
        }
    return dictionary


# Create and view the hurricanes dictionary
hurricane_dictionary = construc_dictionary(names, months, years, max_sustained_winds, areas_affected, update_damages, deaths)
for hurricane, data in hurricane_dictionary.items():
    print(hurricane," : ",data)
# 3
# Organizing by Year
def organize_hurricanes_by_year(hurricane_data):
    hurricanes_by_year = {}
    for hurricane, data in hurricane_data.items():
        year = data['Year']
        if year not in hurricanes_by_year:
            hurricanes_by_year[year] = []
        hurricanes_by_year[year].append(data)
    return hurricanes_by_year


# create a new dictionary of hurricanes with year and key
hurricanes_by_year = organize_hurricanes_by_year(hurricane_dictionary)
for year, hurricanes in hurricanes_by_year.items():
    print(year, ":")
    for hurricane in hurricanes:
        print("\t", hurricane)

# 4
# Counting Damaged Areas
from collections import defaultdict
def count_by_area(hurricane_data):
    count = defaultdict(int)
    for data in hurricane_data.values():
        area_affected = data.get("Area Affected", "Not found")
        for area in area_affected:
            count[area] +=1
    return count

# create dictionary of areas to store the number of hurricanes involved in
area_count = count_by_area(hurricane_dictionary)
for area, count in area_count.items():
    print(area,":",count)

# 5
# Calculating Maximum Hurricane Count
def most_affected_area(area_count):
    max_area = None
    max_area_count = 0
    for area,count in area_count.items():
        if count > max_area_count:
            max_area = area
            max_area_count = count
    return max_area, max_area_count
# find most frequently affected area and the number of hurricanes involved in
most_affected, count = most_affected_area(area_count)
print("The most affected area is:", most_affected)
print("Number of hurricanes affecting the area:", count)

# 6
# Calculating the Deadliest Hurricane
def most_deadly_hurricane(hurricane_data):
    max_mortality_hurricane = None
    max_mortality = 0
    for hurricane,data in hurricane_data.items():
        if data["Death"] > max_mortality:
            max_mortality = data["Death"]
            max_mortality_hurricane = hurricane
    return max_mortality_hurricane, max_mortality

# find highest mortality hurricane and the number of deaths
deadliest, deaths = most_deadly_hurricane(hurricane_dictionary)
print("The deadliest hurricane is:", deadliest)
print("Number of deaths caused by the hurricane:", deaths)
# 7
# Rating Hurricanes by Mortality
mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def rating_mortality(hurricane_data):
    mortality_hurricane = {scale: [] for scale in mortality_scale}

    for hurricane,data in hurricane_data.items():
        deaths = data["Death"]
        for scale,threshold in mortality_scale.items():
            if deaths <= threshold:
                mortality_hurricane[scale].append(data)
                break
    return mortality_hurricane

# categorize hurricanes in new dictionary with mortality severity as key
hurricanes_by_mortality = rating_mortality(hurricane_dictionary)
for rating, hurricanes in hurricanes_by_mortality.items():
    print("Mortality Rating:", rating)
    for hurricane in hurricanes:
        print("\t", hurricane)

# 8 Calculating Hurricane Maximum Damage
def find_maximum_damage(hurricane_data):
    maximum_damage_hurricane = None
    maximum_damage = 0
    for hurricane, data in hurricane_data.items():
        if data["Damage"]=="Damages not recorded":
            continue
        if data["Damage"] > maximum_damage:
            maximum_damage = data["Damage"]
            maximum_damage_hurricane = hurricane
    return maximum_damage_hurricane, maximum_damage
# find highest damage inducing hurricane and its total cost
maximum_damage_hurrican, maximum_damage = find_maximum_damage(hurricane_dictionary)
print("The most damage hurricane is:", maximum_damage_hurrican)
print("Number of damage caused by the hurricane:", maximum_damage)

# 9
# Rating Hurricanes by Damage
#0 means not recorded
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def rating_damages(hurricane_dictionary):
    hurricane_damage = {scale: [] for scale in damage_scale}
    for key, value in hurricane_dictionary.items():
        damage = value["Damage"]
        for scale,threshold in damage_scale.items():
            if damage == "Damages not recorded":
                damage = 0
            if damage <= threshold:
                hurricane_damage[scale].append(value)
                break
    return hurricane_damage
# categorize hurricanes in new dictionary with damage severity as key
hurrincane_by_damage = rating_damages(hurricane_dictionary)
for rating, hurricanes in hurrincane_by_damage.items():
    print("Damage rating:", rating)
    for hurricane in hurricanes:
        print("\t", hurricane)
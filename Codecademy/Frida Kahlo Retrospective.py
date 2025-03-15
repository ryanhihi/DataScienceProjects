painting_names = ["The Two Fridas", "My Dress Hang Here", "Tree of Hope", "Self Portrait With Monkeys"]
dates = [1939, 1933, 1946, 1940]

# Combine dates and painting names into a list of tuples
paintings = list(zip(dates, painting_names))

# Add new paintings
paintings.append([1944, "The Broken Column"])
paintings.append([1946, "The Wounded Deer"])
paintings.append([1937, "Me and My Doll"])

print(paintings)

# Calculate the length of the paintings list
num_paintings = len(paintings)
print("Number of paintings:", num_paintings)

# Generate audio tour numbers
audio_tour_numbers = list(range(1, num_paintings + 1))
print("Audio tour numbers:", audio_tour_numbers)

# Combine audio tour numbers, dates, and painting names into a list of tuples
master_list = list(zip(audio_tour_numbers, dates, painting_names))
print("Master list:", master_list)

tricky = ["c", "C",  65, 197]
print(list(tricky.sort()))
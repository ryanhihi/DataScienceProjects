import pandas as pd
import numpy as np
import seaborn as sns
import statsmodels
import matplotlib.pyplot as plt
import math

## Read in Data
flight = pd.read_csv("flight.csv")
print(flight.head())
print(flight.info())

## Task 1
plt.hist(flight.coach_price)
plt.show()
plt.clf()
#Calculate the mean, median
print(flight.coach_price.mean())
print(flight.coach_price.median())

#500 seems not an ideal price ticket since it falls into the far right part of the distribution plot

## Task 2
#plot the histogram for ticket prices for flights that are 8 hours long
sns.histplot(flight.coach_price[flight.hours == 8])
plt.show() # Show the plot
plt.clf() # Clear the plot

#Calculate the mean,median of this subset data:
print(np.mean(flight.coach_price[flight.hours == 8]))
print(np.median(flight.coach_price[flight.hours == 8]))

## Task 3
#Innitial visualization for delay
plt.hist(flight.delay)
plt.show()
plt.clf()
#The hisgrogram seem out of place because of the outliers
#Investigate the range and diustribution of delay
print(flight.delay.mean())
print(flight.delay.min())
print(flight.delay.max())

print("\nUnique delay values and their counts:")
flight_delay_counts = flight.delay.value_counts()
for value, count in flight_delay_counts.items():
    print(f"{value}: {count}")

# As the count variable display, the delay more than 50 min can be considered outliers, so those observations will be removed from the visual

sns.histplot(flight.delay[(flight.delay <=50) & (flight.delay >0)] )
plt.show()
plt.clf()

## Task 4
#Visual that shows the relationship between coach and first-class prices
plt.scatter(flight.coach_price, flight.firstclass_price)
plt.show()
plt.clf()

#There are too many points to see the relationship, added opacity and LOWESS to the plot
sns.lmplot(x='coach_price', y='firstclass_price', data=flight, line_kws={'color': 'black'}, lowess=True)
plt.show()
plt.clf()
#Do flights with higher coach prices always have higher first-class prices as well?
# There is a strong positive linear relationship between the 2 variables firstclass_price and coach_price

## Task 5
# What is the relationship between coach prices and inflight features— inflight meal, inflight entertainment, and inflight WiFi? Which features are associated with the highest increase in price?

#Using group boxplot for visualization
sns.boxplot(x="inflight_meal", y="coach_price", data=flight)
plt.title("Coach Price vs Inflight Meal")
plt.xlabel("Inflight Meal")
plt.ylabel("Coach Price")
plt.show()

sns.boxplot(x="inflight_entertainment", y="coach_price", data=flight)
plt.title("Coach Price vs Inflight Entertainment")
plt.xlabel("Inflight Entertainment")
plt.ylabel("Coach Price")
plt.show()

sns.boxplot(x="inflight_wifi", y="coach_price", data=flight)
plt.title("Coach Price vs Inflight WiFi")
plt.xlabel("Inflight WiFi")
plt.ylabel("Coach Price")
plt.show()

## Task 6
#How does the number of passengers change in relation to the length of flights?
#Initial Visualization using scatterplot
plt.scatter(flight.hours, plt.passengers )
plt.show()
plt.clf()

#Filter the outliers for clear visuals:
# Scatter plot for flights with duration less than 6 hours and passengers less than 180
plt.scatter(flight.hours[(flight.hours < 6) & (flight.passengers < 180)], flight.passengers[(flight.hours < 6) & (flight.passengers < 180)])
plt.title('Flights with Duration < 6 hours and Passengers < 180')
plt.xlabel('Flight Hours')
plt.ylabel('Passengers')
plt.show()
plt.clf()

# Scatter plot for flights with duration greater than 6 hours and passengers less than 180
plt.scatter(flight.hours[(flight.hours > 6) & (flight.passengers < 180)], flight.passengers[(flight.hours > 6) & (flight.passengers < 180)])
plt.title('Flights with Duration > 6 hours and Passengers < 180')
plt.xlabel('Flight Hours')
plt.ylabel('Passengers')
plt.show()
plt.clf()

## Task 7
#Visualize the relationship between coach and first-class prices on weekends compared to weekdays.

# Create a subset of the data for better visualization
sampled_data = flight.sample(frac=0.5)

plt.figure(figsize=(12, 6))
sns.scatterplot(x='coach_price', y='firstclass_price', hue='weekend', data=sampled_data, palette='coolwarm')
plt.title('Coach Price vs First-Class Price (Weekdays vs Weekends)')
plt.xlabel('Coach Price')
plt.ylabel('First-Class Price')
plt.legend(title='Weekend', loc='upper left')
plt.grid(True)
plt.show()

## Task 8

# Create a boxplot of coach prices by day of the week with hue for redeyes
plt.figure(figsize=(12, 6))
sns.boxplot(x='day_of_week', y='coach_price', hue='redeye', data=data, palette='Set2')
plt.title('Coach Prices by Day of the Week and Redeye Status')
plt.xlabel('Day of the Week')
plt.ylabel('Coach Price')
plt.legend(title='Redeye', loc='upper right')
plt.grid(True)
plt.show()
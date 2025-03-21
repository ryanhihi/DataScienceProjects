from matplotlib import pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

visits_per_month = [9695, 7909, 10831, 12942, 12495, 16794, 14161, 12762, 12777, 12439, 10309, 8724]

# numbers of limes of different species sold each month
key_limes_per_month = [92.0, 109.0, 124.0, 70.0, 101.0, 79.0, 106.0, 101.0, 103.0, 90.0, 102.0, 106.0]
persian_limes_per_month = [67.0, 51.0, 57.0, 54.0, 83.0, 90.0, 52.0, 63.0, 51.0, 44.0, 64.0, 78.0]
blood_limes_per_month = [75.0, 75.0, 76.0, 71.0, 74.0, 77.0, 69.0, 80.0, 63.0, 69.0, 73.0, 82.0]


# create your figure here
plt.figure(figsize=(12,8))
ax1 = plt.subplot(1,2,1)
plt.plot(range(len(months)),visits_per_month, marker="o")
plt.xlabel("Month")
plt.ylabel("Total Visits")
ax1.set_xticks(range(len(months)))
ax1.set_xticklabels(months)
plt.title("Visits per month")


ax2 = plt.subplot(1,2,2)
plt.plot(range(len(months)),key_limes_per_month, color ="green")
plt.plot(range(len(months)),persian_limes_per_month, color ="orange")
plt.plot(range(len(months)),blood_limes_per_month, color ="black")
plt.legend(["Key Limes","Persian Limes","Blood Limes"])
ax2.set_xticks(range(len(months)))
ax2.set_xticklabels(months)
plt.title("Sales by Catergory")

plt.show()
plt.savefig('My charts')

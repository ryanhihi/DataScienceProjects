import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

sales = pd.read_csv('product_sales.csv')

print(sales.info())

print(sales.week.value_counts())


plt.figure(figsize=(10, 6))
sns.histplot(sales['week'], bins=len(sales['week'].unique()), kde=False)
plt.xlabel('Week')
plt.ylabel('Count')
plt.title('Product Sales by Week')
plt.show()

print(sales.sales_method.value_counts())
# Perform claining sales_method
sales['sales_method'] = sales['sales_method'].replace('email', 'Email')
sales['sales_method'] = sales['sales_method'].replace('em + call', 'Email + Call')
print(sales.sales_method.value_counts())

print(sales.nb_sold.value_counts())

print(sales.revenue.min())
print(sales.revenue.max())

#Handling missing values with revenue using Linear Regression

X_known = sales[['nb_sold']][~sales['revenue'].isnull()]
y_known = sales[['revenue']][~sales['revenue'].isnull()]

X_missing = sales[['nb_sold']][sales['revenue'].isnull()]




model = LinearRegression()
model.fit(X_known, y_known)

predicted_revenue = model.predict(X_missing)

sales.loc[sales['revenue'].isnull(), 'revenue'] = predicted_revenue

print(sales.info())

plt.scatter(sales['nb_sold'], sales['revenue'])
plt.show()

#yearS_as_customer
print(sales.years_as_customer.value_counts())
#remove outlier

sales = sales[~sales['years_as_customer'].isin([63, 47])]
print(sales.info())

#nb_site_visits:
print(sales['nb_site_visits'].min())
print(sales['nb_site_visits'].max())
print(sales['nb_site_visits'].value_counts())

#State:

print(sales['state'].value_counts())

#visualize selling methods:
plt.figure(figsize=(8, 6))
sns.countplot(x='sales_method', data=sales)
plt.title('Count of Sales Method')
plt.xlabel('Sales Method')
plt.ylabel('Count')
plt.show()

sales_method_counts = sales['sales_method'].value_counts()
plt.figure(figsize=(8, 6))
plt.pie(sales_method_counts, labels=sales_method_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Sales Methods')
plt.show()

#Visualize the spread of revenue
plt.figure(figsize=(8, 6))
sns.histplot(sales['revenue'], bins='auto')
plt.title('Distribution of Revenue')
plt.xlabel('Revenue')
plt.ylabel('Frequency')
plt.show()

print(sales['revenue'].describe())

#Visualize the revenue by each approach
plt.figure(figsize=(8, 6))
sns.boxplot(x= sales['sales_method'], y = sales['revenue'], data=sales)
plt.title('Revenue by Sales Method')
plt.xlabel('Sales Method')
plt.ylabel('Revenue')
plt.show()
print('Sales by Email:')
sales_by_email = sales[sales['sales_method'] == "Email"]
print(sales_by_email['revenue'].describe())
print('Sales by Call:')
sales_by_call = sales[sales['sales_method'] == "Call"]
print(sales_by_call['revenue'].describe())
print('Sales by Mix:')
sales_by_mix = sales[sales['sales_method'] == "Email + Call"]
print(sales_by_mix['revenue'].describe())

#Time series for sales by methods.

revenue_over_time = sales.groupby(['week', 'sales_method'])['revenue'].sum().reset_index()
plt.figure(figsize=(12, 8))
sns.lineplot(x='week', y='revenue', hue='sales_method', data=revenue_over_time, marker='o')
plt.title('Revenue Over Time by Sales Method')
plt.xlabel('Week')
plt.ylabel('Revenue')
plt.legend(title='Sales Method')
plt.show()

# Group by week and calculate total revenue
total_revenue_by_week = sales.groupby('week')['revenue'].sum().reset_index()

# Summary Statistics of total revenue by week
summary_stats = total_revenue_by_week['revenue'].describe()
print(summary_stats)

# Histogram of total revenue by week
plt.figure(figsize=(8, 6))
sns.histplot(total_revenue_by_week['revenue'], bins='auto')
plt.title('Distribution of Total Revenue by Week')
plt.xlabel('Total Revenue')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.histplot(data=sales, x='revenue', hue='sales_method', element='step', stat='density', common_norm=False)
plt.title('Distribution of Revenue by Sales Method')
plt.xlabel('Revenue')
plt.ylabel('Density')
plt.show()
sales_methods = sales['sales_method'].unique()
for method in sales_methods:
    subset_data = sales[sales['sales_method'] == method]

    # Create count plot for years_as_customer
    plt.figure(figsize=(8, 6))
    sns.countplot(data=subset_data, x='years_as_customer')
    plt.title(f'Count of Customers by Years as Customer for {method}')
    plt.xlabel('Years as Customer')
    plt.ylabel('Count')
    plt.show()

    # Create count plot for week
    plt.figure(figsize=(8, 6))
    sns.countplot(data=subset_data, x='week')
    plt.title(f'Count of Customers by Week for {method}')
    plt.xlabel('Week')
    plt.ylabel('Count')
    plt.show()

    # Create count plot for sales_method (redundant as it shows only one type of sales_method)
    plt.figure(figsize=(8, 6))
    sns.countplot(data=subset_data, x='sales_method')
    plt.title(f'Count of Customers by Sales Method for {method}')
    plt.xlabel('Sales Method')
    plt.ylabel('Count')
    plt.show()

state_counts = sales['state'].value_counts()

top_states_call = sales[sales['sales_method'] == 'Call']['state'].value_counts().nlargest(5)
plt.figure(figsize=(8, 8))
plt.pie(top_states_call, labels=top_states_call.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Customers by State for Call Sales Method')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

top_states_email = sales[sales['sales_method'] == 'Email']['state'].value_counts().nlargest(5)
plt.figure(figsize=(8, 8))
plt.pie(top_states_email, labels=top_states_email.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Customers by State for Email Sales Method')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

top_states_mix = sales[sales['sales_method'] == 'Email + Call']['state'].value_counts().nlargest(5)
plt.figure(figsize=(8, 8))
plt.pie(top_states_mix, labels=top_states_mix.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Customers by State for Mix Sales Method')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

revenue_by_method = sales.groupby('sales_method')['revenue'].sum()

# Plotting pie chart
plt.figure(figsize=(8, 8))
plt.pie(revenue_by_method, labels=revenue_by_method.index, autopct='%1.1f%%', startangle=140)
plt.title('Revenue Distribution by Sales Method')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()
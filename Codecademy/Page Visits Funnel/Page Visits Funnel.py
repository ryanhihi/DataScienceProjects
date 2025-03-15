import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])
print(visits.head(10))
print(cart.head(10))
print(checkout.head(10))

visits_cart = visits.merge(cart, how='left')
print(len(visits_cart))

time_stamp_null = visits_cart[visits_cart.cart_time.isnull()]
print(len(time_stamp_null))

#What percent of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart?
required_percentage = float(len(time_stamp_null) / len(visits_cart) * 100)
print("The percent of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart: ")
print(required_percentage)

cart_purchase = cart.merge(purchase, how='left')
print(cart_purchase)
checkout_null = cart_purchase[cart_purchase.purchase_time.isnull()]
print(len(checkout_null))
required_percentage1 = float(len(checkout_null) / len(cart_purchase) * 100)
print("The percentage of users put items in their cart, but did not proceed to checkout:")
print(required_percentage1)

#Merge all four steps of the funnel, in order, using a series of left merges. Save the results to the variable all_data.

#Examine the result using print and head.

all_data = visits.merge(cart, how='left').merge(checkout, how='left').merge(purchase, how='left')
print(all_data.head(5))

#What percentage of users proceeded to checkout, but did not purchase a t-shirt?
check_out_no_purchase = all_data[(all_data.purchase_time.isnull()) & (all_data.checkout_time.notna())]
print(check_out_no_purchase)
required_percentage2 = float(len(check_out_no_purchase)/len(all_data) * 100)
print("The percentage of users proceeded to checkout, but did not purchase a t-shirt:")
print(required_percentage2)


print("Summary")
print("The percent of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart: ", required_percentage)
print("The percentage of users put items in their cart, but did not proceed to checkout:",required_percentage1)
print("The percentage of users proceeded to checkout, but did not purchase a t-shirt:",required_percentage2)

#Which step of the funnel is weakest (i.e., has the highest percentage of users not completing it)?
#How might Cool T-Shirts Inc. change their website to fix this problem?
print("Which step of the funnel is weakest? - visits - checkout")

#Using the giant merged DataFrame all_data that you created, let’s calculate the average time from initial visit to final purchase. Add a column that is the difference between purchase_time and visit_time.
all_data['total_time'] = all_data.purchase_time - all_data.visit_time
print(all_data.total_time)
mean_total_time = all_data.total_time.mean()

print("The average time purchase is: ", mean_total_time)
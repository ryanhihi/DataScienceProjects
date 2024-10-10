#Examine the first few rows of ad_clicks.
import pandas as pd
ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head(5))

#Your manager wants to know which ad platform is getting you the most views.
#How many views (i.e., rows of the table) came from each utm_source?
utm_source_views = ad_clicks.groupby('utm_source').user_id.count().reset_index()
print(utm_source_views)

#If the column ad_click_timestamp is not null, then someone actually clicked on the ad that was displayed.
#Create a new column called is_click, which is True if ad_click_timestamp is not null and False otherwise.
ad_clicks['is_click'] = ~ad_clicks\
   .ad_click_timestamp.isnull()

#We want to know the percent of people who clicked on ads from each utm_source.
#Start by grouping by utm_source and is_click and counting the number of user_id‘s in each of those groups. Save your answer to the variable clicks_by_source.
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

#Now let’s pivot the data so that the columns are is_click (either True or False), the index is utm_source, and the values are user_id.
clicks_pivot = clicks_by_source.pivot(index='utm_source', columns='is_click', values='user_id').reset_index()
print(clicks_pivot)
clicks_pivot['percent_clicked'] = clicks_pivot[True]/(clicks_pivot[True]+clicks_pivot[False])

#Analyzing A/B test
#The column experimental_group tells us whether the user was shown Ad A or Ad B.
#Were approximately the same number of people shown both ads?
group_ab=ad_clicks.groupby('experimental_group').user_id.count().reset_index()
print(group_ab)

#Using the column is_click that we defined earlier, check to see if a greater percentage of users clicked on Ad A or Ad B.
ab_is_clicked = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()
print(ab_is_clicked)
ab_is_clicked_pivot = ab_is_clicked.pivot(index='experimental_group', columns='is_click', values='user_id').reset_index()
print(ab_is_clicked_pivot)

#The Product Manager for the A/B test thinks that the clicks might have changed by day of the week.
#Start by creating two DataFrames: a_clicks and b_clicks, which contain only the results for A group and B group, respectively.
a_clicks = ad_clicks[ad_clicks.experimental_group=='A'].reset_index()
b_clicks = ad_clicks[ad_clicks.experimental_group=='B'].reset_index()

#For each group (a_clicks and b_clicks), calculate the percent of users who clicked on the ad by day.
a_group_click_byday = a_clicks.groupby(['is_click','day']).user_id.count().reset_index()
a_group_click_byday_pivot = a_group_click_byday.pivot(index='day', columns='is_click', values='user_id').reset_index()
a_group_click_byday_pivot['percent-clicked'] = a_group_click_byday_pivot[True]/(a_group_click_byday_pivot[False]+a_group_click_byday_pivot[True])
print(a_group_click_byday_pivot)

b_group_click_byday = b_clicks.groupby(['is_click','day']).user_id.count().reset_index()
b_group_click_byday_pivot = b_group_click_byday.pivot(index='day', columns='is_click', values='user_id').reset_index()
b_group_click_byday_pivot['percent-clicked'] = b_group_click_byday_pivot[True]/(b_group_click_byday_pivot[False]+b_group_click_byday_pivot[True])
print(b_group_click_byday_pivot)
# Merge the two pivot tables on the 'day' column
combined_pivot = pd.merge(a_group_click_byday_pivot, b_group_click_byday_pivot, on='day', suffixes=('_A', '_B'))

print(combined_pivot)
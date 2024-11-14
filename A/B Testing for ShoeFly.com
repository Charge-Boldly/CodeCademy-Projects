import codecademylib3
import pandas as pd

# Load the ad_clicks data
ad_clicks = pd.read_csv('ad_clicks.csv')

# Check the columns of the dataframe to identify the correct timestamp column
print(ad_clicks.columns)

# Assuming 'ad_click_timestamp' is the correct column name for timestamp
# Handle invalid date formats by coercing errors to NaT
ad_clicks['ad_click_timestamp'] = pd.to_datetime(ad_clicks['ad_click_timestamp'], errors='coerce')

# Create the is_click column
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

# Extract the day of the week from the timestamp column
ad_clicks['day'] = ad_clicks['ad_click_timestamp'].dt.day_name()

# Group by experimental_group, is_click, and day, then count user_id for each combination
clicks_by_day = ad_clicks.groupby(['experimental_group', 'is_click', 'day']).user_id.count().reset_index()

# Pivot the data to get separate columns for clicks (True) and non-clicks (False)
clicks_by_day_pivot = clicks_by_day.pivot_table(
    index=['experimental_group', 'day'],
    columns='is_click',
    values='user_id',
    aggfunc='sum'
).reset_index()

# Print the shape and columns of the pivoted DataFrame to check the structure
print(clicks_by_day_pivot.shape)
print(clicks_by_day_pivot.columns)

# Adjust column renaming based on the actual structure
# The pivoted DataFrame will have columns: 'experimental_group', 'day', and a boolean column (True for clicks)
clicks_by_day_pivot.columns = ['experimental_group', 'day', 'clicks']

# If 'clicks' is missing for some groups (i.e., no True values for 'is_click'), we can fill it with 0
clicks_by_day_pivot['clicks'].fillna(0, inplace=True)

# Add 'no_clicks' by subtracting 'clicks' from the total counts
clicks_by_day_pivot['no_clicks'] = clicks_by_day_pivot.groupby(['experimental_group', 'day'])['clicks'].transform('sum') - clicks_by_day_pivot['clicks']

# Calculate the percentage of clicks for each day and ad group (Ad A or Ad B)
clicks_by_day_pivot['percent_clicked'] = clicks_by_day_pivot['clicks'] / (clicks_by_day_pivot['clicks'] + clicks_by_day_pivot['no_clicks']) * 100

# Display the final result with the percentage of clicks by day and ad group
print(clicks_by_day_pivot)

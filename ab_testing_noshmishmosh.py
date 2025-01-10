# Step 1: Import the noshmishmosh library
import noshmishmosh

# Step 2: Import numpy as np
import numpy as np

# Step 4: Get the list of all visitors
all_visitors = noshmishmosh.customer_visits

# Step 5: Get the list of paying visitors
paying_visitors = noshmishmosh.purchasing_customers

# Step 6: Calculate the lengths of the lists
total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)

# Step 7: Calculate the baseline percent
baseline_percent = paying_visitor_count / total_visitor_count * 100

# Step 8: Print the baseline percent
print(f"Baseline Conversion Rate: {baseline_percent:.2f}%")

# Step 9: Get the list of money spent by customers
payment_history = noshmishmosh.money_spent

# Step 10: Calculate the average payment per paying customer
average_payment = np.mean(payment_history)

# Step 11: Calculate the number of new customers needed to generate $1240 in additional revenue
new_customers_needed = np.ceil(1240 / average_payment)

# Step 12: Calculate the percentage point increase required
percentage_point_increase = new_customers_needed / total_visitor_count * 100
print(f"Percentage Point Increase: {percentage_point_increase:.2f}%")

# Step 13: Calculate the minimum detectable effect (MDE)
mde = percentage_point_increase / baseline_percent * 100

# Step 14: Print the MDE
print(f"Minimum Detectable Effect: {mde:.2f}%")

# Step 15: Set the statistical significance threshold
statistical_significance = 10  # 10%

# Step 16: Use the A/B sample size calculator (manually or via a library) to calculate the required sample size
# Assuming the A/B sample size calculator is used:
# ab_sample_size = calculate_sample_size(baseline_percent, mde, statistical_significance)

# Placeholder for illustrative purposes:
ab_sample_size = "Use a calculator to find this number."

print(f"Sample Size Needed for A/B Testing: {ab_sample_size}")

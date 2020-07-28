# Load Modules
import os
import csv

# Define path variables
file_name = "budget_data.csv"
path = "Resources"
file = os.path.join(path, file_name)

# Define calculation variables
total_months = 0
net_total = 0
previous_budget = 0
average_change = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_date = ""
greatest_decrease_date = ""

# Open file
with open(file) as csv_file:
    csv_file.readline()
    reader = csv.reader(csv_file)

    # Define change variables
    change_count = 0
    change = 0

# Loop
    for row in reader:
        total_months += 1
        current_budget = int(row[1])
        net_total += current_budget
        
        # Set budget conditional
        if previous_budget != 0:
            change = current_budget-previous_budget
            average_change += change
            change_count += 1
        previous_budget = current_budget

        # Set greatest_increase conditional
        if change > greatest_increase:
            greatest_increase = change
            greatest_increase_date = row[0]

        # Set greatest_decrease conditional
        if change < greatest_decrease:
            greatest_decrease = change
            greatest_decrease_date = row[0]

# Define f-string deliverable with markdown & variable calculations 
output = f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total:,}
Average  Change: ${average_change/change_count:.2f}
Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase:,})
Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease:,})
"""
# Deliver output
print(output)

# Create writeable file
with open('output.txt', 'w') as output_file:
    output_file.write(output)
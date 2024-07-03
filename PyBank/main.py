import os
import csv
#hello world
# Set path for the input CSV file
csvpath = os.path.join("", "Resources", "budget_data.csv")

# Initialize variables
total_months = 0
net_total = 0
previous_profit_loss = 0
total_change = 0
greatest_increase = 0
greatest_decrease = 0
greatest_increase_date = ""
greatest_decrease_date = ""

# Output directory
output_file = os.path.join("" , "analysis", "financial_analysis.txt")

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header row
    csv_header = next(csvreader)

    # Read each row on csv file
    for row in csvreader:
        
        # Count for months
        total_months += 1
        
        # Net total amount of "Profit/Losses"
        current_profit_loss = int(row[1])
        net_total += current_profit_loss
        
        # Calculate change in profit/loss
        if total_months > 1:
            change = current_profit_loss - previous_profit_loss
            total_change += change
            # Track greatest increase and decrease
            if change > greatest_increase:
                greatest_increase = change
                greatest_increase_date = row[0]
            if change < greatest_decrease:
                greatest_decrease = change
                greatest_decrease_date = row[0]

        # Update previous profit/loss for next iteration
        previous_profit_loss = current_profit_loss

# Calculate average change
if total_months > 1:
    average_change = total_change / (total_months - 1)

# Format the average change (2 decimal places)
average_change = round(average_change, 2)

# The analysis output
analysis_output = f"""
Financial Analysis

----------------------------

Total Months: {total_months}

Total: ${net_total}

Average Change: ${average_change}

Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})

Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})

"""

# Print analysis to terminal
print(analysis_output)


# Export the analysis results to a text file
with open(output_file, "w") as txtfile:
    txtfile.write(analysis_output)

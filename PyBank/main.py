import os
import csv

# Define the file path 
#budget_csv = os.path.join("..", 'Resources', "budget.csv")
#budget_csv = os.path.join('/Users/pandari/Desktop/KP/edXData/UofM-VIRT-DATA-PT-03-2024-U-LOLC/python-challenge/PyBank/Resources/budget_data.csv')
budget_csv = os.path.join('python-challenge', 'PyBank', 'Resources', 'budget_data.csv')


# Initialize variables
total_months = 0
total_profit_loss = 0
previous_profit_loss = 0
profit_loss_changes = []
months = []

# Read the CSV file
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader)  # Skip header row

    for row in csvreader:
        # Extract data
        date = row[0]
        profit_loss = int(row[1])

        # Calculate total months and total profit/loss
        total_months += 1
        total_profit_loss += profit_loss

        # Calculate profit/loss change
        if total_months > 1:
            change = profit_loss - previous_profit_loss
            profit_loss_changes.append(change)
            months.append(date)

        previous_profit_loss = profit_loss

# Calculate average change
average_change = sum(profit_loss_changes) / (total_months - 1)

# Find greatest increase and decrease in profits
greatest_increase = max(profit_loss_changes)
greatest_decrease = min(profit_loss_changes)
increase_month = months[profit_loss_changes.index(greatest_increase)]
decrease_month = months[profit_loss_changes.index(greatest_decrease)]

# Print results to terminal
print("Financial Analysis")
print("-------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_loss}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})")

# Export results to a text file
#output_file = os.path.join("..", 'analysis', "financial_analysis.txt")
output_file = os.path.join('python-challenge/PyBank/analysis/financial_analysis.txt')

with open(output_file, 'w') as txtfile:
    txtfile.write("Financial Analysis\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit_loss}\n")
    txtfile.write(f"Average Change: ${average_change:.2f}\n")
    txtfile.write(f"Greatest Increase in Profits: {increase_month} (${greatest_increase})\n")
    txtfile.write(f"Greatest Decrease in Profits: {decrease_month} (${greatest_decrease})\n")

print(f"Results exported to {output_file}")

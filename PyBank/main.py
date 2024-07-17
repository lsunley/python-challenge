import os
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Declare variables
total_months = 0
total_net = 0
max_increase = 0
max_increase_month = ""
max_decrease = 0
max_decrease_month = ""
previous_profit = 0
total_change = 0

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    header = next(csvreader)
    
    # Loop through entire data set
    for row in csvreader:
        # Counter to track how many entries
        total_months += 1
        # Sum the total in Column B
        total_net += int(row[1])

        current_month = row[0]  
        current_profit = int(row[1])  
        
        # Calculate change in profit since the last row
        if previous_profit != 0:
            profit_change = current_profit - previous_profit
            total_change += profit_change

            # Check for greatest increase in profits
            if profit_change > max_increase:
                max_increase = profit_change
                max_increase_month = current_month
            
            # Check for greatest decrease in profits
            if profit_change < max_decrease:
                max_decrease = profit_change
                max_decrease_month = current_month
        
        # Update previous_profit to current_profit for next iteration
        previous_profit = current_profit

# Calculate average change
average_change = total_change / (total_months - 1)  # Exclude the first row since there's no previous profit to compare with

# Define function to print and write
def print_and_write(text, file):
    print(text)
    file.write(text + '\n')
    
# Write financial analysis results to a text file
output_path = os.path.join(os.getcwd(), 'output.txt')
with open(output_path, 'w') as file:
    print_and_write("Financial Analysis", file)
    print_and_write("\n--------------------------", file)
    print_and_write(f"\nTotal Months: {total_months}", file)
    print_and_write(f"\nTotal: ${total_net}", file)
    print_and_write(f"\nAverage Change: ${average_change:.2f}", file)
    print_and_write(f"\nGreatest Increase in Profits: {max_increase_month} (${max_increase})", file)
    print_and_write(f"\nGreatest Decrease in Profits: {max_decrease_month} (${max_decrease})", file)

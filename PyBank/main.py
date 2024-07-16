# Modules
import os
import csv

# Prompt user for title lookup
date = input("Which date? ")

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Set variable to check if we found the date
found = False

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Loop through looking for the video
    for row in csvreader:
        #3/10/2024
        if date in row[0]:
            print("On date: " + row[0] + " profit/loss was  " + row[1] )

            # Set variable to confirm we have found the video
            found = True    
    
        # If the date is never found, alert the user
    if found is False:
        print("Sorry about this, we don't seem to have what you are looking for!")

# Count total amount of months (length of column A)
# The total number of months included in the dataset 

print("Total Months: \n")

# The net total amount of "Profit/Losses" over the entire period
print("Total: ")

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
print("Average Change: ")

# The greatest increase in profits (date and amount) over the entire period
print("Greatest Increase in Profits: ")

# The greatest decrease in profits (date and amount) over the entire period
print("Greatest Decrease in Profits: ")
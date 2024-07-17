import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join("Resources", "election_data.csv")

# Initialize variables
total_votes = 0         # Column A
candidate_votes = {}    
candidates = []         # Column C
winner = ""
winner_votes = 0

# Read the CSV file
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row
    header = next(csvreader)
    
    # Count total votes and collect votes per candidate
    for row in csvreader:
        total_votes += 1
        
        candidate_name = row[2]  
        
        # Add candidate to the list if not already added
        if candidate_name not in candidates:
            candidates.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1

# Determine the winner
for candidate in candidate_votes:
    votes = candidate_votes[candidate]
    if votes > winner_votes:
        winner_votes = votes
        winner = candidate

# Calculate the percentage of votes each candidate won
results = []
for candidate in candidates:
    votes = candidate_votes[candidate]
    percentage = (votes / total_votes) * 100
    results.append(f"{candidate}: {percentage:.3f}% ({votes})")

# Print and write the election results
with open('output.txt', 'w') as file:
    # Print to terminal and write to file
    def print_and_write(text):
        print(text)
        file.write(text + '\n')

    print_and_write("Election Results")
    print_and_write("\n-------------------------")
    print_and_write(f"\nTotal Votes: {total_votes}")
    print_and_write("\n-------------------------\n")
    for i, result in enumerate(results):
        print_and_write(result)
        # Print a blank line after each result, except the last one
        if i < len(results) - 1:
            print_and_write("")
    print_and_write("\n-------------------------")
    print_and_write(f"\nWinner: {winner}")
    print_and_write("\n-------------------------")



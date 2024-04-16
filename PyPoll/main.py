import os
import csv

# Define the file path for election data
#election_csv = os.path.join("..", 'Resources', "election_data.csv")
#election_csv = os.path.join('/Users/pandari/Desktop/KP/edXData/UofM-VIRT-DATA-PT-03-2024-U-LOLC/python-challenge/PyPoll/Resources/election_data.csv')
election_csv = os.path.join('python-challenge', 'PyPoll', 'Resources', 'election_data.csv')

# Initialize variables
total_votes = 0
candidate_votes = {}  # Dictionary to store candidate votes

# Read the CSV file
with open(election_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Skip header row

    for row in csvreader:
        # Extract data
        voter_id, county, candidate = row

        # Update total votes
        total_votes += 1

        # Update candidate votes
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the percentage of votes for each candidate
candidate_percentages = {}
for candidate, votes in candidate_votes.items():
    candidate_percentages[candidate] = (votes / total_votes) * 100

# Determine the winner
winner = max(candidate_votes, key=candidate_votes.get)

# Print results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {candidate_percentages[candidate]:.2f}% ({votes})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")


# Export results to a text file
#output_file = os.path.join("..", 'analysis', "election_results.txt")
output_file = os.path.join('python-challenge/PyPoll/analysis/election_results.txt')
with open(output_file, 'w') as txtfile:
    txtfile.write("Election Results\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write("-------------------------\n")
    for candidate, votes in candidate_votes.items():
        txtfile.write(f"{candidate}: {candidate_percentages[candidate]:.2f}% ({votes})\n")
    txtfile.write("-------------------------\n")
    txtfile.write(f"Winner: {winner}\n")
    txtfile.write("-------------------------\n")

print(f"Results exported to {output_file}")

# Load Modules
import os
import csv

csv_path = os.path.join('Resources', 'election_data.csv')

# Define a Function for % calculation
def cal_percentage(part, whole):
    return 100 * (part / whole)

# Define calculation variables
total_vote = 0
khan_votes = 0
correy_votes = 0
otooley_votes = 0
li_votes = 0
max_votes = 0

# Open and read CSV file
with open(csv_path, newline='') as csv_file:
    rows = csv.reader(csv_file, delimiter=',')

    # Read the header row first
    csv_header = next(rows)

    # Loop
    for row in rows:

        # Set candidate conditional
        if row[2] == "Khan":
            khan_votes += 1
        elif row[2] == "Correy":
            correy_votes += 1
        elif row[2] == "O'Tooley":
            otooley_votes += 1    
        elif row[2] == "Li":
            li_votes += 1

        # Total Vote Count

        total_vote += 1

# Define a dictionary with candidates and votes

dict_candidates_and_votes = {
    "Khan": khan_votes, 
    "Correy": correy_votes,
    "O'Tooley": otooley_votes,
    "Li": li_votes
    }

# Find winner
for candidate, votes in dict_candidates_and_votes.items():
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# # Display results
print(f"Election Results")
print(f"-----------------------------")
print(f"Total Votes: {total_vote}")
print(f"-----------------------------")
print(f"Khan: {cal_percentage(khan_votes,total_vote):.3f}%  ({khan_votes})")
print(f"Correy: {cal_percentage(correy_votes,total_vote):.3f}%  ({correy_votes})")
print(f"Li: {cal_percentage(li_votes,total_vote):.3f}%  ({li_votes})")
print(f"O\'Tooley: {cal_percentage(otooley_votes,total_vote):.3f}%  ({otooley_votes})")
print(f"------------------------------")
print(f"Winner: {winner}")
print(f"------------------------------")

# Export a text file with the results
with open('Election_Results.txt', 'w') as txtwriter:
    txtwriter.write("Election Results" + "\n")
    txtwriter.write("--------------------------" + "\n")
    txtwriter.write(f"Total Votes: {total_vote}" + "\n")
    txtwriter.write("--------------------------" + "\n")
    txtwriter.write(f"Khan: {cal_percentage(khan_votes,total_vote):.3f}%  ({khan_votes})" + "\n")
    txtwriter.write(f"Correy: {cal_percentage(correy_votes,total_vote):.3f}%  ({correy_votes})" + "\n")
    txtwriter.write(f"Li: {cal_percentage(li_votes,total_vote):.3f}%  ({li_votes})" + "\n")
    txtwriter.write(f"O\'Tooley: {cal_percentage(otooley_votes,total_vote):.3f}%  ({otooley_votes})" + "\n")
    txtwriter.write("--------------------------" + "\n")
    txtwriter.write(f"Winner: {winner}" + "\n")
    txtwriter.write("--------------------------" + "\n")
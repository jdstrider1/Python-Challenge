import os
import csv

current_dir = os.path.dirname(os.path.realpath(__file__))  # Get the current working directory
file_path = os.path.join(current_dir, 'Resources', 'election_data.csv')  # Construct the absolute file path to the CSV file

# Build lists from csv file necessary for analysis
ballot_ids = []
counties = []
candidates = []
total_votes = 0
candidates_votes = {} # Set this variable as dictionary so we can keep track of different candidates

# Read the CSV file
with open(file_path, 'r') as file:
    csv_reader = csv.DictReader(file)
    
    # Execute function for analysis
    for row in csv_reader:
        total_votes += 1 # Keep count of rows
        candidate = row['Candidate'] # Set variable for desired column 
        
        # Count the votes for each candidate
        if candidate in candidates_votes:
            candidates_votes[candidate] += 1
        else:
            candidates_votes[candidate] = 1

winner = max(candidates_votes, key=candidates_votes.get) # Set winner as element in dictionary with maximum value

# Print desired results of analysis
print("Election Results")
print("------------------------")

# Use count of rows to show total amount of votes
print(f"Total number of votes cast: {total_votes}")

print("------------------------")

# Calculate and display the percentage of votes each candidate won
for candidate, votes in candidates_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.3f}% ({votes} votes)") # Print results in desired format
    
print("------------------------")

print(f"Winner: {winner}") # Print result of winner

print("------------------------")

folder_name = "Analysis"
output_file = "election_analysis.txt"
file_path = os.path.join(current_dir, folder_name, output_file)  # Construct the absolute file path for the output file

with open(file_path, 'w') as output:  # Open the file for writing
    output.write("Election Results\n")
    output.write("------------------------\n")
    output.write(f'Total number of votes cast: {total_votes}\n')
    output.write(f'------------------------\n')
    for candidate, votes in candidates_votes.items():
         percentage = (votes / total_votes) * 100
         output.write(f'{candidate}: {percentage:.3f}% ({votes} votes)\n')
    output.write("------------------------\n")
    output.write(f'Winner: {winner}\n')
    output.write("------------------------\n")

print(f"Election analysis has been exported to {output_file}")



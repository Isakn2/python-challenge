import os
import csv

# Path for the input CSV file
csvpath = os.path.join("", "Resources", "election_data.csv")

# Output directory
output_file = os.path.join("" , "analysis", "election_results.txt")

# To count the total number of votes.
total_votes = 0
# Dictionary to count votes for each candidate.
candidate_votes = {}

# Open the CSV using the UTF-8 encoding
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip header
    csv_header = next(csvreader)

    # Read each row on csv file
    for row in csvreader:
        # For each row, increments total votes
        total_votes += 1
        
        # Get candidate name from the row
        candidate_name = row[2]
        
        # If the candidate has other votes, then add a vote, else initialize the vote count
        if candidate_name in candidate_votes:
            # Adds votes for each candidate in the candidate_votes dictionary.
            candidate_votes[candidate_name] += 1
        else:
            candidate_votes[candidate_name] = 1

# Determine the winner based on max function
winner = max(candidate_votes, key=candidate_votes.get)

# The analysis output format as requested
analysis_output = f"""
Election Results

-------------------------

Total Votes: {total_votes}

-------------------------

"""
# Iteration over dictionary items: append each candidate results
# Loops through each tuple, unpacking the candidate's name into "candidate" and the corresponding vote count into "votes".
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    # {percentage:.3f} inserts the percentage of votes the candidate received, formatted to three decimal places.
    analysis_output += f"{candidate}: {percentage:.3f}% ({votes})\n\n"
    # \n adds a newline character, so each candidate's information is printed on a new line (in this case is double spaced).

analysis_output += f"-------------------------\n\nWinner: {winner}\n\n-------------------------\n"

# Print analysis to terminal
print(analysis_output)

# Export the analysis results to a text file
with open(output_file, "w") as txtfile:
    txtfile.write(analysis_output)

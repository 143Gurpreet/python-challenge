# Incorporated the csv module
import csv
import os

# Files to load:
csv_path = os.path.join("Resources", "election_data.csv")
ANALYSIS_PATH = os.path.join("analysis", "financial_analysis.txt")
# start up variables
total_votes = 0
candidates = {}

# Read the csv:
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(csv_path) as election_data:
    csv_reader = csv.reader(election_data)

#skip the header row
    header=next(csv_reader)    

# Loop through each row in the CSV file
    for row in csv_reader:
        
        # Increment the total number of votes
        total_votes += 1
        
        # Get the candidate name
        candidate_name = row[2]

       
        
         # add the candidate name ,if has not been added 
        if candidate_name not in candidates:
            candidates[candidate_name] = 1
        else:
            # If already added , increment their vote count
            candidates[candidate_name] += 1

# Find the winner
winner = max(candidates, key=candidates.get)

# Print the analysis to the terminal
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
for candidate, votes in candidates.items():
    percentage = (votes / total_votes)*100
    print(f"{candidate}: {round(percentage,3)}% ({votes})")
print(f"-------------------------")
print(f"Winner: {winner}")
print(f"-------------------------")

# Export the analysis to a text file
with open(ANALYSIS_PATH, "w") as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        file.write(f"{candidate}: {round(percentage,3)}% ({votes})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")

    
   
    




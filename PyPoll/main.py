# First we'll import the os module
import os
# Module for reading csv file
import csv

path_of_file = 'C:/Users/lucyh/OneDrive/Desktop/Boot Camp/02-Homework/03-Python/Resources'
csvpath = os.path.join(path_of_file, 'election_data.csv')
# Export a text file with the results
file_output = "results.txt"
output = ""

# Open the file and read csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    # Variables
    total_votes = 0
    candidate_votes = dict()
    candidate = ""
    winner = ""
    winner_votes = 0

    # Loops
    for row in csvreader:
        total_votes += 1

        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1


    csvfile.close()

    output = "Election Results\n" + \
            "----------------------------\n" + \
            f"Total Votes: {total_votes}\n" + \
            "----------------------------\n" 
            
    for candidate_name, votes in candidate_votes.items():
        percent = (votes / total_votes) * 100
        output += f"{candidate_name}: {percent:.3f}% ({votes})\n"
        if votes > winner_votes: 
            winner_votes = votes
            winner = candidate_name

    output += "----------------------------\n" 
    output += f"Winner: {winner}\n"
    output += "----------------------------\n"   

    # Print results to the terminal
    print(output)

# Export a text file with the results
with open(file_output, 'w') as txt_file:
    txt_file.write(output)
    
    txt_file.close()
 

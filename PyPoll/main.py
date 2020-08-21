# PyPoll Homework
# Import the os module
import os
import csv

# Module for reading CSV Files
import csv

csvpath = os.path.join("Resources", "election_data.csv")

# Read CSV file
# with open (csvpath, 'r') as file_handler:
#  lines = file_handler.read ()
#  print(lines)
#  print(type(lines))


with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter =",")

    # Skip header Voter ID, County, and Candidate
    election_header = next(csvreader)

    # Create list for candidate 
    # Create dictionary to capture Candidate and their votes
    candidate = []
    votes = {}
    i = 0

    # Loop through election data file to store data in candidate list and election dictionary
    for row in csvreader:
        i += 1
        if row[2] in candidate and row[2] not in 'candidate':
            votes[row[2]] = votes[row[2]] + 1
        else:
            candidate.append(row[2])
            votes[row[2]] = 1


# Calculate Total Votes from votes dictionary
total_votes = sum(votes.values())

# Get results for votes dictionary
key_list = list(votes.keys())
val_list = list(votes.values())


# Print Election Results, Calculate Percentages and Winner in Terminal
print("Election Results")
print('------------------------------------')
print("Total Votes: " + str(total_votes))
print('------------------------------------')

# Calculate Votes Percentages

percent0 = round((val_list[0] / total_votes) * 100, 3)
percent1 = round((val_list[1] / total_votes) * 100, 3)
percent2 = round((val_list[2] / total_votes) * 100, 3)
percent3 = round((val_list[3] / total_votes) * 100, 3)


print(key_list[0] +": " + str(percent0) + "% " + "(" +str(val_list[0]) + ")")
print(key_list[1] +": " + str(percent1) + "% " + "(" +str(val_list[1]) + ")")
print(key_list[2] +": " + str(percent2) + "% " + "(" +str(val_list[2]) + ")")
print(key_list[3] +": " + str(percent3) + "% " + "(" +str(val_list[3]) + ")")
print('------------------------------------')

# Show Election Results Winner
maxwin = max(votes, key=votes.get)
print("Winner: " + maxwin)
print('------------------------------------')

# Specify the file to write to electionresults.csv in Analysis folder
output_path = os.path.join("Analysis", "electionresults.csv")

# Open the file using "write" mode
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (colum headers)
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['----------------------------------'])
    csvwriter.writerow(["Total Votes:  " + str(total_votes)])
    csvwriter.writerow(['------------------------------------'])
    csvwriter.writerow([key_list[0] +":  " + str(percent0) + "%  " + "(" +str(val_list[0]) + ")"])
    csvwriter.writerow([key_list[1] +":  " + str(percent1) + "%  " + "(" +str(val_list[1]) + ")"])
    csvwriter.writerow([key_list[2] +":  " + str(percent2) + "%  " + "(" +str(val_list[2]) + ")"])
    csvwriter.writerow([key_list[3] +":  " + str(percent3) + "%  " + "(" +str(val_list[3]) + ")"])
    csvwriter.writerow(['----------------------------------'])
    csvwriter.writerow(["Winner:   " + maxwin])
    csvwriter.writerow(['----------------------------------'])






        




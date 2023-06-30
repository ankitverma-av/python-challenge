
# Importing OS and CSV modules 
import os
import csv

# Setting the path for the file 
csvpath = os.path.join(r"C:\Users\abc\Desktop\python-Challenge\PyPoll\Resources\election_data.csv")

# Open the CSV
with open(csvpath) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    csv_header = next(csv_reader)
    
    total_votes = 0
    candidates_votes = {}
    winner_count = 0
    percent_candidates_votes = {}
    
    # Loop through looking for canditates
    for row in csv_reader:

        # The total number of votes cast
        total_votes = total_votes + 1
        
        # A complete list of candidates who received votes and The total number of votes each candidate won
        if row[2] in candidates_votes:
            candidates_votes[row[2]] += 1
        else:
            candidates_votes[row[2]] = 1
            
        # The percentage of votes each candidate won
        
        for key, value in candidates_votes.items():
            percent_candidates_votes[key] =round((value/total_votes)* 100 , 3)
        
        # The winner of the election based on popular vote.
            if percent_candidates_votes[key] > winner_count:
                winner_count = candidates_votes[key]
                winner = key
    
# print the result on terminal    
print(f"Election Results")

print(f"-------------------------")

print(f"Total Votes: {total_votes}")

print(f"-------------------------")

for key, velue in candidates_votes.items():
    print(key,':' , str(percent_candidates_votes[key]),'%','  ','(',candidates_votes[key],')')

print(f"-------------------------")

print(f"Winner: {winner}")

print(f"-------------------------")

# open the output file and write the result to the csv
with open(r"C:\Users\abc\Desktop\python-Challenge\PyPoll\Analysis\output.txt","w") as text:

    text.write(f"Election Results\n")

    text.write(f"-------------------------\n")

    text.write(f"Total Votes: {total_votes}\n")

    text.write("-------------------------\n")

    for key, velue in candidates_votes.items():
        text.write(f"{key}: {str(percent_candidates_votes[key])}%   ({candidates_votes[key]})\n")

    text.write(f"-------------------------\n")

    text.write(f"Winner: {winner}\n")

    text.write(f"-------------------------\n")
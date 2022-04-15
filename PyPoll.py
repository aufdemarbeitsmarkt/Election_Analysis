import csv 
import os 

## 3.5.5

# Assign a variable to load a file from a path.
file_to_load = os.path.join('Resources', 'election_results.csv')

# Assign a variable to save the file to a path.
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# initialize a total vote counter, candidate_options list, candidate_votes dictionary
total_votes = 0
candidate_options = []
candidate_votes = {}

# winning candidate and winning count tracker
winning_candidate = ''
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # read and print the header row
    headers = next(file_reader)

    # print each row in the csv file
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        # create list of candidates' names, add 0 to vote counts for candidate_votes
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        
        # add a vote to the candidate_votes dictionary
        candidate_votes[candidate_name] += 1
    
    # iterate through the candidate list, retrieve vote count, calculate vote_percentage
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = votes / total_votes * 100


        #  To do: print out each candidate's name, vote count, and percentage of votes to the terminal.
        print(f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')


        # Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # if true then set winning_count = votes and winning_percent = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
            # set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name
    
    winning_candidate_summary = (
        f'-------------------------\n'
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage:.1f}%\n'
        f'-------------------------\n'
    )

    print(winning_candidate_summary)
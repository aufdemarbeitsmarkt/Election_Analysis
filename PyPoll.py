import csv 
import os 

## 3.6.3

# assign a variable to load a file from a path.
file_to_load = os.path.join('Resources', 'election_results.csv')

# assign a variable to save the file to a path.
file_to_save = os.path.join('analysis', 'election_analysis.txt')

# initialize a total vote counter, candidate_options list, candidate_votes dictionary
total_votes = 0
candidate_options = []
candidate_votes = {}

# track the winning candidate, winning count, and winning percentage 
winning_candidate = ''
winning_count = 0
winning_percentage = 0

# open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # read the header row
    headers = next(file_reader)
    # iterate over each row in the csv file
    for row in file_reader:
        total_votes += 1
        candidate_name = row[2]
        # create list of candidates' names, add 0 to vote counts for candidate_votes
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        # add a vote to the candidate_votes dictionary
        candidate_votes[candidate_name] += 1
    
with open(file_to_save, 'w') as txt_file:
    # print and save to our text file the election results
    election_results = (
        f'Election Results\n'
        f'-------------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'-------------------------\n'
    )
    print(election_results, end='')
    txt_file.write(election_results)

    # iterate through the candidate list, retrieve vote count, calculate vote_percentage
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = votes / total_votes * 100
        #  print out each candidate's name, vote count, and percentage of votes to the terminal
        candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
        print(candidate_results, end='')
        # save the candidate results to our text file
        txt_file.write(candidate_results)

        # determine if the votes are greater than the winning count
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

    # print and save to our text file the winning candidate's results
    print(winning_candidate_summary, end='')
    txt_file.write(winning_candidate_summary)

import os
import csv

# Creating directory path for the election data csv
election_path = os.path.join('Resources', 'election_data.csv')

with open(election_path, 'r') as csvfile:
    election = csv.reader(csvfile, delimiter=',')
    header = next(election)
    
    # Set initial values 
    total = 0
    unique_candidates = []
    candidate_list = []
    votes_won = []
    percent_won = []
    
    for row in election:
        # Total number of votes cast
        total += 1 # Incrementing total number of votes by 1 each row
        # Turning column 3 into a list
        candidate_list.append(row[2])
        # Complete list of candidates who reveived votes
        if row[2] not in unique_candidates:
            unique_candidates.append(row[2]) # Only appending the candidate name if it has not appeared before
    
    # Running through the list-version of column 3
    for candidate in set(candidate_list):
        # Total number of votes each candidate won
        votes_won.append(candidate_list.count(candidate)) # Counting the number of times each candidate appears
        # Percentage of votes each candidate won
        percent_won.append((candidate_list.count(candidate)/total) * 100) # Calculating percentage for each candidate from their number of votes vs the total
        
    # Winner of the election based on popular vote
    winner = votes_won.index(max(votes_won)) # Obtaining the index where the maximum number of votes won appears in the list
    winner_name = unique_candidates[winner] # Obtaining the name corresponding to the winner index number
    
    print('Election Results')
    print('----------------------')
    print(f'Total Votes: {total}')
    print('----------------------')
    print(f'{unique_candidates[0]}: {round(percent_won[0], 3)}% ({votes_won[0]})')
    print(f'{unique_candidates[1]}: {round(percent_won[1], 3)}% ({votes_won[1]})')
    print(f'{unique_candidates[2]}: {round(percent_won[2], 3)}% ({votes_won[2]})')
    print('----------------------')
    print(f'Winner: {winner_name}')
    print('----------------------')
    
# Creating directory path for the output data
output_path = os.path.join('Analysis', 'output.txt')

with open(output_path, 'w') as output:
    # The data to be printed
    text = (
        'Election Results\n'
        '----------------------\n'
        f'Total Votes: {total}\n'
        '----------------------\n'
        f'{unique_candidates[0]}: {round(percent_won[0], 3)}% ({votes_won[0]}\n'
        f'{unique_candidates[1]}: {round(percent_won[1], 3)}% ({votes_won[1]})\n'
        f'{unique_candidates[2]}: {round(percent_won[2], 3)}% ({votes_won[2]})\n'
        '----------------------\n'
        f'Winner: {winner_name}\n'
        '---------------------\n'
    )
    
    # Adding the data to the txt file
    output.write(text)
    
    print(output)
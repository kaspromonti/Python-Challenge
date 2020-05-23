
# Import dependencies

import os
import csv
from collections import Counter

# Point to reader file to import
poll_read_file = os.path.join('Resources/election_data.csv')

with open(poll_read_file, encoding="utf8") as poll_data:
    poll_reader = csv.reader(poll_data, delimiter=',')
    poll_header = next(poll_reader)

# Creating List for each column
    voter_id = []
    candidates = []
    county = []

# Appending Lists with column data
    for row in poll_reader:
        voter_id.append(row[0])
        county.append(row[1])
        candidates.append(row[2])

# making dictionary out of candidates where key = candidates : values equals names of candidates
    candidates_dict = {}
    candidates_dict["Candidates"] = candidates
# making dictionary out of counties where key = county : values equals name of county
    county_dict = {}
    county_dict["County"] = county
    
# calculates total vote count using dictionary
    vote_count = 0
    for x in candidates_dict: 
        if isinstance(candidates_dict[x], list): 
            vote_count += len(candidates_dict[x]) 

# Calculating total votes by using the len(method)
    # votes = len(candidates)
    # print(f'****{votes}****')


# Showed all candidate names in list, confirming there are only 4    
    candidate_count = Counter()
    for cand in candidates:
        candidate_count[cand] =+ 1

# Total number of votes by candidate
    
    khan_votes = int(candidates.count("Khan"))
    li_votes = int(candidates.count("Li"))
    otooley_votes = int(candidates.count("O'Tooley"))
    correy_votes = int(candidates.count("Correy"))


# Put vote counts in list so that the max() function could be used to determine the winner

    tallys = [khan_votes, li_votes, otooley_votes, correy_votes]
    winner = max(tallys)
    if float(winner) == khan_votes:
        election_winner = "Khan"
    if float(winner) == li_votes:
        election_winner = "Li" 
    if float(winner) == correy_votes:
        election_winner = "Correy" 
    if float(winner) == otooley_votes:
        election_winner = "O'Tooley" 
  
    khan_percent = format(khan_votes / vote_count, ".02%")
    li_percent = format(li_votes / vote_count, ".02%")
    otooley_percent = format(otooley_votes / vote_count, ".02%")
    correy_percent = format(correy_votes / vote_count, ".02%")

#Printing results in terminal
    print("\n")
    print("====================")
    print("ELECTION RESULTS")
    print("====================")
    print("\n")
    print(f'Total Votes: {vote_count}')
    print(f'Khan: {khan_percent} ({khan_votes})')
    print(f'Correy: {correy_percent} ({correy_votes})')
    print(f'Li: {li_percent} ({li_votes})')
    print(f"O'Tooley: {otooley_percent} ({otooley_votes})")
    print("---------------------")
    print(f'Election Winner: {election_winner}')
    print("---------------------")


#Writing results to output file

#zip lists for output
zipped_results = zip(voter_id, county, candidates)

pypoll_outputfile = os.path.join('Analysis/PyPoll_Output_File.txt')
with open(pypoll_outputfile,'w', newline="") as poll_output:
    pollwriter = csv.writer(poll_output)
    pollwriter.writerow(["====================="])
    pollwriter.writerow(["Election Results"])
    pollwriter.writerow(["====================="])
    pollwriter.writerow([f'Total Votes: {vote_count}'])
    pollwriter.writerow([f'Khan: {khan_percent} ({khan_votes})'])
    pollwriter.writerow([f'Correy: {correy_percent} ({correy_votes})'])   
    pollwriter.writerow([f'Li: {li_percent} ({li_votes})'])   
    pollwriter.writerow([f"O'Tooley: {otooley_percent} ({otooley_votes})"])  
    pollwriter.writerow(["---------------------------------"]) 
    pollwriter.writerow([f'Election Winner: {election_winner}'])
    pollwriter.writerow(["---------------------------------"]) 
    #pollwriter.writerows([poll_header])
    #pollwriter.writerows(zipped_results)




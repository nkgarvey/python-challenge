#import the csv file
import csv
pypoll_csv = "C:/GitHub/python-challenge/pypoll/election_data.csv"
#set variables/lists to count the data
Total_votes = 0
Candidates = []
Candidate_Count = 0
Percent_won = 0
Winner = []
#read in the file
with open(pypoll_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    #determine total votes cast by looping through csv file and counting row[0]
    for row in csvreader:
        Total_votes = Total_votes + 1
        #compile candidate list and candidate vote total
        if row[2] not in Candidates
            Candidates.append(row[2])
            Candidate_Count.append(1)
        else: 
            Candidate_Count + 1
        #determine % of vote for each candidate
    Percent_won = (Candidate_Count/Total_votes)*100,4
    Winner = 

        
        

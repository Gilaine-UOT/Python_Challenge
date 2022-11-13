#!/usr/bin/env python
# coding: utf-8

# In[9]:


## PyPoll Homework Challenge Solution

import os
import csv

csvpath = ".\\PyPoll\\Resources\\election_data.csv"

totalvotes = 0
votepercent = 0

candidatelist = []

candidatedict = {}

## Opening files as csv ##

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)


    for row in csvreader:
        totalvotes += 1

        candidatename = str(row[2])
           
        if candidatename not in candidatelist:
            candidatelist.append(candidatename)
            candidatedict[candidatename] = 0

   
        candidatedict[candidatename] += 1

# Creating a final dictionary of candidate with votes and Printing statements

output = f"""
Election Results
-------------------------
Total Votes: {totalvotes:,}
-------------------------
"""
winner = ""
winningvotes = 0

for candidatename in candidatelist:
    votes = candidatedict[candidatename]
    if votes > winningvotes:
        winner = candidatename
        winningvotes = votes
    votepercent = votes / totalvotes * 100
    output += f"{candidatename}: {votepercent:,.3f}% ({votes}) \n"
output += "------------------------- \n"
output += f"Winner: {winner} \n"
output += "-------------------------"

print(output)

# Output files | Save results

with open(".\\PyPoll\\Resources\\Analysis\\election_data_results.txt", "w") as outputfile:
    outputfile.write(output)


# In[ ]:





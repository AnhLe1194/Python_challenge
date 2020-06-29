#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv
csvpath = os.path.join("Resources", "Homework_03-Python_Instructions_PyPoll_Resources_election_data.csv")


# In[2]:


total_votes = 0
candidates_unique = []
candidate_vote_count = []
percent_count = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    
    for row in csvreader:
        candidate = row[2]
        total_votes = total_votes + 1
        
        if candidate in candidates_unique:
            index = candidates_unique.index(candidate)
            candidate_vote_count[index] = candidate_vote_count[index] + 1
    
        else:
            candidates_unique.append(candidate)
            candidate_vote_count.append(1)

for count in candidate_vote_count:
    percent_count.append(round((count/total_votes)*100, 3))
    max_count = max(candidate_vote_count)


winner = candidates_unique[candidate_vote_count.index(max(candidate_vote_count))]

print(candidates_unique)
print(total_votes)
print(percent_count)
print(candidate_vote_count)
print(winner)


# In[3]:


#To terminal
print(f"Election Results")
print(f"---------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------")
for i in range(len(candidates_unique)):
    print(f"{candidates_unique[i]} : {percent_count[i]}% ({candidate_vote_count[i]})")
print(f"---------------------")
print(f" Winner: {winner}")
print(f"---------------------")


#output txt file
output_file = os.path.join("Analysis","PyPoll__results.txt")
with open(output_file, "w", newline="") as resultfile:
    resultfile.write(f"Election Results")
    resultfile.write(f"---------------------")
    resultfile.write(f"Total Votes: {total_votes}")
    resultfile.write(f"---------------------")
    for i in range(len(candidates_unique)):
        resultfile.write(f"{candidates_unique[i]} : {percent_count[i]}% {candidate_vote_count[i]}")
    resultfile.write(f"---------------------")
    resultfile.write(f" Winner: {winner}")
    resultfile.write(f"---------------------")

   
  


# In[ ]:





# In[ ]:





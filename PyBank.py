#!/usr/bin/env python
# coding: utf-8

# In[30]:


import os
import csv 


# In[31]:


csvpath = os.path.join("Resources", "Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")


# In[32]:


total_months = 0
total_revenue = 0
months = []
total_change = []

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    csv_header = next(csvreader)
    for row in csvreader:
        #print(row)
        total_months = total_months + 1
        total_revenue = total_revenue + int(row[1])
        if total_months == 1:
            prev_rev = int(row[1])
        
        if total_months > 1:
            monthly_change = int(row[1]) - prev_rev
            total_change.append(monthly_change)
            months.append(row[0])
            prev_rev = int(row[1])
            monthly_change = 0


# In[33]:


#print(total_months)
#print(total_revenue)
#print(total_change)


# In[34]:


average_change = round(sum(total_change)/len(months), 2)
#print(average_change)

for i in range(len(total_change)-1):
    max_profit = max(total_change)
    max_loss = min(total_change)
#print(max_profit)
#print(max_loss)

date_max_profit = months[total_change.index(max(total_change))]
#print(date_max_profit)

date_max_loss = months[total_change.index(min(total_change))]
#print(date_max_loss)


# In[36]:


print(f"Financial Analysis")
print(f"--------------------------")
print(f"Your profit is: $ {total_revenue}")
print(f"Total Months: {total_months}")
print(f"Average  Change: ${average_change}")
print(f"Greatest Increase in Profits: {date_max_profit} (${max_profit})")
print(f"Greatest Decrease in Profits: {date_max_loss} (${max_loss})")

#To txt file:
output_file = os.path.join("Analysis", "PyBank_result.txt")
with open(output_file, "w", newline="") as resultfile:
    resultfile.write(f"Financial Analysis")
    resultfile.write(f"--------------------------")
    resultfile.write(f"Your profit is: $ {total_revenue}")
    resultfile.write(f"Total Months: {total_months}")
    resultfile.write(f"Average  Change: ${average_change}")
    resultfile.write(f"Greatest Increase in Profits: {date_max_profit} (${max_profit})")
    resultfile.write(f"Greatest Decrease in Profits: {date_max_loss} (${max_loss})")


# In[ ]:





# In[ ]:





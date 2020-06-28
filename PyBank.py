#!/usr/bin/env python
# coding: utf-8

# In[16]:


import os
import csv 


# In[17]:


csvpath = os.path.join("Homework_03-Python_Instructions_PyBank_Resources_budget_data.csv")


# In[18]:


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


# In[19]:


#print(total_months)
#print(total_revenue)
#print(total_change)


# In[20]:


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


# In[21]:


print(f"Financial Analysis")
print(f"--------------------------")
print(f"Your profit is: $ {total_revenue}")
print(f"Total Months: {total_months}")
print(f"Average  Change: ${average_change}")
print(f"Greatest Increase in Profits: {date_max_profit} (${max_profit})")
print(f"Greatest Decrease in Profits: {date_max_loss} (${max_loss})")


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv


# In[2]:


#path to collect file from resources folder
budgetcsv = os.path.join("PyBank","Resources","budget_data.csv")


# In[3]:


budgetdatacsv = os.path.join("PyBank", "Resources","budget_data.csv")

# Defining variables
total_months = 0
total_value = 0
initial_revenue = 0
net_change_list = []
month_of_change = []
date = []


with open(budgetdatacsv, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    csv.reader(csv_file, delimiter=",")

    header = next(csv_reader)

    # loop through each rows
    for row in csv.reader(csv_file):

        # Track the total months as rows
        total_months = total_months + 1

        date.append(row[0])

        # Track the total value throughout rows
        total_value = total_value + int(row[1])

       
        # Track the revenue changes
        revenue_change = int(row[1]) - (initial_revenue)
       
        # Return the intial value to final value for the next iteration
        initial_revenue = int(row[1])

        # Use append function to store the changes into a new list to calculate the average
        net_change_list.append(revenue_change)

    # As the first iteration net change is useless, using .remove function to remove from the list  
    net_change_list.remove(net_change_list[0])

    # As the first iteration is useless, using .remove function to remove from the list  
    date.remove (date[0])

    # Use sum function to obtain the sum of net change list
    sum_change = (sum(net_change_list))

    # Use len function to obtain the length of date list
    date_length = (len(date))

    # Calculate the average of change and round it to 2 decimals
    average_change = round(sum_change / date_length, 2)

    # Use max and min function to obtain the greatest increase and decrease in the net change list
    greatest_increase = max(net_change_list)
    greatest_decrease = min(net_change_list)

    # Use index function to obtain the date row corresponding row of greatest incease and decrease respectively
    greatest_in_date = date[net_change_list.index(greatest_increase)]
    greatest_de_date = date[net_change_list.index(greatest_decrease)]

# Print out the required information
print('Financial Anaylsis')
print('------------------------')
print("Total Months:", total_months)
print("Total$", total_value)
print("Average_Change:$", average_change)
print("Greatest Increase in Profits:" + " " + str(greatest_in_date) + " "+ "($" + str (greatest_increase)+ ")")
print("Greatest Increase in Profits:" + " " + str(greatest_de_date) + " "+ "($" + str (greatest_decrease)+ ")")

output_path = os.path.join("PyBank", "Resources","Analysis",'budget_data_results.txt')

with open(output_path, 'w') as output:
    output.write('Financial Anaylsis')
    output.write("\n")
    output.write('------------------------')
    output.write("\n")
    output.write("Total Months:" + str(total_months))
    output.write("\n")
    output.write("Total:$" + ' ' +str(total_value))
    output.write("\n")
    output.write("Average_Change:$" + ' ' + str(average_change))
    output.write("\n")
    output.write("Greatest Increase in Profits:" + " " + str(greatest_in_date) + " "+ "($" + str (greatest_increase)+ ")")
    output.write("\n")
    output.write("Greatest Increase in Profits:" + " " + str(greatest_de_date) + " "+ "($" + str (greatest_decrease)+ ")")


# In[ ]:





# Import module and create file path

import os
import csv

# headers = "date, profit_losses"
# headerslist = headers.split(",")

date = []
greatest_loss = ["". 99999999999]
greatest_gain = ["", 0]
month_count = 0 
total_net_value = 0 
net_change_list = []

csvpath = os.path.join('PyBank_budget_data.csv')
with open(csvpath, newline='') as csvfile:
  
   csvreader = csv.reader(csvfile, delimiter=',')
   csv_header = next(csvreader, None)
   first_row = next(csvreader)

# print("Financial Analysis")
# print("------------------")

# Count total number of months in csv

    month_count = month_count + 1
    total_net_value = total_net_value + int(first_row[1])
    previous_net = int(first_row[1])

    for row in csvreader:
        month_count += 1
        total_net_value += int(row[1])
        net_change = int(row[1]) - previous_net
        net_change_list = net_change_list + [net_change]
        previous_net = int(row[1])
        date += [row[0]]
        if net_change > greatest_gain[1]:
            greatest_gain[0] = row[0]
            greatest_gain[1] = net_change
        if net_change < greatest_loss
            greatest_loss[0] = row[0]
            greatest_loss[1] = net_change

# Calculate total net amount of profit/losses

# Calculate average change of profit/losses over entire period 

# Calculate greatest increase in profits with date and amount over entire period

# Calculate greatest decrease in losses with date and amount over entire period

# Export text file with results 

       

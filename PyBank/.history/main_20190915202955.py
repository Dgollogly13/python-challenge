# Import module and create file path

import os
import csv

headers = "date, profit_losses"
headerslist = headers.split(",")

date = []
profit_losses = []

csvpath = os.path.join('PyBank_budget_data.csv')
with open(csvpath, newline='') as csvfile:
  
   csvreader = csv.reader(csvfile, delimiter=',')
   csv_header = next(csvreader, None)

print("Financial Analysis")
print("------------------")

# Count total number of months in csv

rows = list( csv.reader(open('PyBank_budget_data.csv')) )
month_count = len(rows)
for row in rows:
    print(rows)

# Calculate total net amount of profit/losses

# Calculate average change of profit/losses over entire period 

# Calculate greatest increase in profits with date and amount over entire period

# Calculate greatest decrease in losses with date and amount over entire period



       

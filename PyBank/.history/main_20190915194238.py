# Import module and create file path

import os
import csv

headers = "date, profit/losses"
headerslist = headers.split(",")


csvpath = os.path.join('PyBank_budget_data.csv')
with open(csvpath, newline='') as csvfile:
  
   csvreader = csv.reader(csvfile, delimiter=',')
   csv_header = next(csvreader, None)

print("Financial Analysis")
print("------------------")

    for row in csvreader:
       

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

for row sum(1 for row in csv.reader( open('PyBank_budget_data.csv') ) ):
    print (row) 



       

import os
import csv

csvpath = os.path.join('.', 'resources', "budget_data_1.csv)")

print(csvpath)

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    print(csvfile)

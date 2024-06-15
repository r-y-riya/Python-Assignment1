import csv

with open("data.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(', '.join(row))

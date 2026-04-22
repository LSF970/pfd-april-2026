# Script to turn csv data into Python Dictionary

import csv

rows = []

with open("employers.csv", newline="") as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        print(row["Name"], row["email"]) # Just give values of keys stated
        print(row) # Gives each row as a dictionary

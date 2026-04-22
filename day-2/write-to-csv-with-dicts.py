# Writing to a csv file with dicts

# Import csv module
import csv

# Create lists for csv
header = ["Name", "Age"]
data = [["Alex", 25, "A"], ["Brad", 30, "C"], ["Joey", 18, "B"]]

with open("student_info.csv", mode="w", newline="") as csvfile:
    csvwriter = csv.DictWriter(csvfile, fieldnames=header) # create csvwriter object

    csvwriter.writeheader()
    for student in data:
        csvwriter.writerow({"Name": student[0], "Age": student[1]})
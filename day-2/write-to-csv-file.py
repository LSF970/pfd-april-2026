# Writing to a csv file

# Import csv module
import csv

# Create lists for csv
header = ["Name", "Age"]
data = [["Alex", 25], ["Brad", 30], ["Joey", 18]]

# Open csv file, write data to csv
with open("student_info.csv", mode="w", newline="") as csvfile:
    csvwriter = csv.writer(csvfile) # create csvwriter object
    csvwriter.writerow(header) # write the header
    csvwriter.writerows(data) # write the rows
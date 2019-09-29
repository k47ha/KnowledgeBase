import csv
import json

with open('CDD.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='\t')
    for row in reader:
        header = row.keys()
    with open("CDD_cleaned.csv", mode="w") as outfile:
        csv_columns = header
        writer = csv.DictWriter(outfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in reader:
            writer.writerow(data)

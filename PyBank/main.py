## load in budget_data.csv file
import os
import csv

budget_data = os.path.join('Documents', 'BootCamp', 'Trilogy', 'Repos', 'utsa-san-data-pt-06-2020-u-c', 'Homework', '03-Python', 'Instructions', 'PyBank','Resources','budget_data')

with open (budget_data) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csv_reader)
    print(f'Header: {csv_header}')

    # for i in csv_reader:




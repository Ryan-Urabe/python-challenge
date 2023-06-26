import os
import csv

budget_data_csv = os.path.join('..', 'Resources', 'budget_data.csv')

def run_analysis(data):
    print('hi')



with open(budget_data_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    print(csvreader)
    run_analysis(csvreader)


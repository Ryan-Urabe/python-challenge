import os
import csv

election_data = os.path.join('..', 'Resources', 'election_data.cvs')

with open(election_data, 'r') as csvfile:
    csvreader = csv,reader(csvfile, deliminter=',')

    header = next(csvreader)

    print(csvreader)
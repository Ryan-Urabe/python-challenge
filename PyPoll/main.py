import os
import csv

election_data = os.path.join("Resources", "election_data.csv")

def election_results(data):
    information = []
    for row in data:
        list = [info for info in row]
        information.append(list)
    
    total_votes = 0
    candidates = []


    for vote in information:
        candidate = []
        total_votes += 1
        if len(candidates) < 1:
            candidate.append(vote[2])
            candidate.append(1)
            candidates.append(candidate)
        

        number = len(candidates)

        for i in range(number):
            
            if vote[2].upper() == candidates[i][0].upper():
                candidates[i][1] += 1

            else:
                number -= 1
                if number == 0:
                    candidate.append(vote[2])
                    candidate.append(1)
                    candidates.append(candidate)

    length = len(candidates)                
    winner = candidates[0]
    
    print('Election Results\n')
    for i in range(20):
        print('-', end='')
    print(f'\n\nTotal Votes: {total_votes}\n')
    for i in range(20):
        print('-', end='')
    print('\n')
    for i in range(length):
        if candidates[i][1] > winner[1]:
            winner = candidates[i]
        percentage = round((candidates[i][1] / total_votes)*100, 3)
        print(f'\n{candidates[i][0]}: {percentage}% ({candidates[i][1]})\n')
    for i in range(20):
        print('-', end='')
    print(f'\n\nWinner: {winner[0]}\n')
    for i in range(20):
        print('-', end='')
    print('\n')

    with open(os.path.join('analysis', 'Election Results'), 'w') as output:
        output.write('Election Results\n')
        output.write('------------------------------------\n')
        output.write(f'Total Votes: {total_votes}\n')
        output.write('------------------------------------\n')
        for i in range(length):
            percentage = round((candidates[i][1] / total_votes)*100, 3)
            output.write(f'{candidates[i][0]}: {percentage}% ({candidates[i][1]})\n')
        output.write('------------------------------------\n')
        output.write(f'Winner: {winner[0]}\n')
        output.write('------------------------------------')


with open(election_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    election_results(csvreader)
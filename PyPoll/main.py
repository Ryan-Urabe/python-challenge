import os
import csv

# line 5 stores csv path in variable
election_data = os.path.join("Resources", "election_data.csv")

def election_results(data):                             # defining fn to analyze data from csv
    information = []                                    # define list variable to store data from csv in
    for row in data:                                    # Loop to store data from csv in list
        list = [info for info in row]
        information.append(list)
    

    total_votes = 0                                     # creates variable to hold total number of votes
    candidates = []                                     # creaets list that will store candidates


    for vote in information:                            # loop to look at each list of data in information
        candidate = []                                  # creates empty list meant to store one candidates data
        total_votes += 1                                # counts total votes
        if len(candidates) < 1:                         # if statement to see if there are no candidates yet observed, if so it adds one using the first data seen
            candidate.append(vote[2])
            candidate.append(1)
            candidates.append(candidate)
        

        number = len(candidates)                        # since len() doesnt work for lists when trying to for loop for it, need a variable to store length, variable will also help with skipping candidates not currently observed

        for i in range(number):                         # loop to check if candidate has been observed yet and loops for the amount of candidates observed 
                                                        # I am aware that dictionaries could make this way simplier but I couldn't find the answer
            if vote[2].upper() == candidates[i][0].upper():     # checks if candidate has been observed, if so adds vote to counter for candidate
                candidates[i][1] += 1

            else:
                number -= 1                             # a unique way of doing things here. when only one candidate has been observed, the else statement wont be triggered. but if more than 1 have been observed, then i need this to skip candidates in list that don't match the current observed candidate
                                                        # its a very unnecessarily convoluted way of going about it, but it works
                if number == 0:                         
                    candidate.append(vote[2])
                    candidate.append(1)
                    candidates.append(candidate)

    length = len(candidates)                            # same thing as line 27        
    winner = candidates[0]                              # variable for winner info
    
    # lines 46 to 63 are formatting for terminal output
    print('Election Results\n')
    for i in range(20):
        print('-', end='')
    print(f'\n\nTotal Votes: {total_votes}\n')
    for i in range(20):
        print('-', end='')
    print('\n')
    for i in range(length):
        if candidates[i][1] > winner[1]:                # it statement to find candidate with most votes
            winner = candidates[i]
        percentage = round((candidates[i][1] / total_votes)*100, 3)     # formula to get percentage of vote that candidates achieved
        print(f'\n{candidates[i][0]}: {percentage}% ({candidates[i][1]})\n')
    for i in range(20):
        print('-', end='')
    print(f'\n\nWinner: {winner[0]}\n')
    for i in range(20):
        print('-', end='')
    print('\n')

    # line 65 creaetes a text file and allows for writing in it, lines 66 to 76 are formatting
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


with open(election_data, 'r') as csvfile:               # opens csv 
    csvreader = csv.reader(csvfile, delimiter=',')      # seperates data from csv by a ',' and puts it into one big list variable

    header = next(csvreader)                            # takes header out of reading data

    election_results(csvreader)                         # calls function from before using the csv data
import os
import csv

# line 5 stores csv path in variable
budget_data_csv = os.path.join("Resources", "budget_data.csv")

def run_analysis(data):                             # defining fn to analyze data from csv
    information = []                                # define list variable to store data from csv in
    for row in data:                                # Loop to store data from csv in list
        list = [info for info in row]
        information.append(list)
    
            
    # lines 15-23 define variables
    months = 0                              
    total_budget = 0
    previous = int(information[0][1])               # previous is a variable that will be used to calculate change
    current_change = 0
    change = 0
    greatest_increase = 0
    month_increase = information[0][0]
    greatest_decrease = 0
    month_decrease = information[0][0]

    for info in information:                        # loop to go through all the data stored in 'information' 
        months = months + 1                         # calculates number of months in data
        total_budget = total_budget + int(info[1])  # adds profits (losses) from each month
        current_change = (int(info[1]) - previous)  # current change is a variable used in two situations, calculating monthly change and finding greatest increase/decrease
        change = change + current_change
        previous = int(info[1])                     # sets preiovus to current data profit as its no longer needed in this loop but is needed for next month loop
        if current_change > greatest_increase:      # finds greatest increase
            greatest_increase = current_change
            month_increase = info[0]
        elif current_change < greatest_decrease:    # finds greatest decrease
            greatest_decrease = current_change
            month_decrease = info[0]

    average = round(change / (months - 1), 2)       # average calculation

    # from lines 41 to 48 is formating to print desired information to terminal
    print('Financial Analysis\n')                   
    for i in range(20):                             # loops '-' to not have to type '---------------------'
        print('-', end='')
    print('\n\nTotal Months: ' + str(months))
    print('\nTotal: $' + str(total_budget))
    print('\nAverage Change: $' + str(average))
    print('\nGreatest Increase in Profits: ' + month_increase + ' ($' + str(greatest_increase) + ')')
    print(f'\nGreatest Decrease in Profits: {month_decrease} (${greatest_decrease})')

    # line 52 creaetes a text file and allows for writing in it, lines 52 to 58 are formatting
    with open(os.path.join('analysis', 'Financial_Analysis_Output.txt'), 'w') as output:
        output.write('Financial Analysis\n')
        output.write('------------------------------------\n')
        output.write(f'Total Months: {months}\n')
        output.write(f'Total: ${total_budget}\n')
        output.write(f'Average Change: ${average}\n')
        output.write(f'Greatest Increase in Profits: {month_increase} (${greatest_increase})\n')
        output.write(f'Greatest Decrease in Profits: {month_decrease} (${greatest_decrease})\n')

with open(budget_data_csv, "r") as csvfile:         # opens csv 
    csvreader = csv.reader(csvfile, delimiter=',')  # seperates data from csv by a ',' and puts it into one big list variable

    header = next(csvreader)                        # takes header out of reading data

    run_analysis(csvreader)                         # calls function from before using the csv data

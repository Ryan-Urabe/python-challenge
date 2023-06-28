import os
import csv

budget_data_csv = os.path.join("Resources", "budget_data.csv")


def run_analysis(data):
    information = []
    for row in data:
        list = [info for info in row]
        information.append(list)
    
            

    months = 0
    total_budget = 0
    previous = int(information[0][1])
    current_change = 0
    change = 0
    greatest_increase = 0
    month_increase = information[0][0]
    greatest_decrease = 0
    month_decrease = information[0][0]
    for info in information:
        months = months + 1
        total_budget = total_budget + int(info[1])
        current_change = (int(info[1]) - previous)
        change = change + current_change
        previous = int(info[1])
        if current_change > greatest_increase:
            greatest_increase = current_change
            month_increase = info[0]
        elif current_change < greatest_decrease:
            greatest_decrease = current_change
            month_decrease = info[0]
    average = round(change / (months - 1), 2)

    print('Financial Analysis\n')
    for i in range(20):
        print('-', end='')
    print('\n\nTotal Months: ' + str(months))
    print('\nTotal: $' + str(total_budget))
    print('\nAverage Change: $' + str(average))
    print('\nGreatest Increase in Profits: ' + month_increase + ' ($' + str(greatest_increase) + ')')
    print(f'\nGreatest Decrease in Profits: {month_decrease} (${greatest_decrease})')

    with open(os.path.join('analysis', 'Financial_Analysis_Output.txt'), 'w') as output:
        output.write('Financial Analysis\n')
        output.write('------------------------------------\n')
        output.write(f'Total Months: {months}\n')
        output.write(f'Total: ${total_budget}\n')
        output.write(f'Average Change: ${average}\n')
        output.write(f'Greatest Increase in Profits: {month_increase} (${greatest_increase})\n')
        output.write(f'Greatest Decrease in Profits: {month_decrease} (${greatest_decrease})\n')

with open(budget_data_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)

    run_analysis(csvreader)

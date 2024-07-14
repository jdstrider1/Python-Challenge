import os
import csv

current_dir = os.path.dirname(os.path.realpath(__file__))  # Get the current working directory
file_path = os.path.join(current_dir, 'Resources', 'budget_data.csv')  # Construct the absolute file path to the CSV file

total_months = 0
net_total = 0
changes = []
average_change = 0

with open(file_path, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    previous_profit = 0
    max_increase = 0
    max_increase_date = ""
    max_decrease = 0
    max_decrease_date = ""

    for row in csv_reader:
        total_months += 1
        net_total += int(row[1])

        current_profit = int(row[1])
        change = current_profit - previous_profit
        changes.append(change)
        current_date = row[0]

        if change > max_increase:
            max_increase = change
            max_increase_date = current_date

        if change < max_decrease:
            max_decrease = change
            max_decrease_date = current_date

        previous_profit = current_profit

    average_change = sum(changes[1:]) / (len(changes) - 1)

print("Financial Analysis")
print("------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${net_total}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {max_increase_date} (${max_increase})')
print(f'Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})')

folder_name = "Analysis"
output_file = "financial_analysis.txt"
file_path = os.path.join(current_dir, folder_name, output_file)  # Construct the absolute file path for the output file

with open(file_path, 'w') as output:  # Open the file for writing
    output.write("Financial Analysis\n")
    output.write("------------------------\n")
    output.write(f'Total Months: {total_months}\n')
    output.write(f'Total: ${net_total}\n')
    output.write(f'Average Change: ${average_change:.2f}\n')
    output.write(f'Greatest Increase in Profits: {max_increase_date} (${max_increase})\n')
    output.write(f'Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n')

print(f"Financial analysis has been exported to {output_file}")
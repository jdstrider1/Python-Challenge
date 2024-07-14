import os
import csv

total_months = 0 # Set starting values for calcuations as 0
net_total = 0
changes = []
average_change = 0

with open('Resources/budget_data.csv', 'r') as file: # Open CSV file with correct filepath
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    previous_profit = 0 # Set starting point for profit as 0
    max_increase = 0 # Set starting greatest profit as 0
    max_increase_date = "" # Allows tracking of date of greatest profit so far
    max_decrease = 0 # Set starting lowest profit as 0
    max_decrease_date = "" # Allows tracking of date of lowest profit so far

    for row in csv_reader:
        total_months += 1 # Sum up the number of months
        net_total += int(row[1]) # Sum up the changes in profit/loss over the entire period

        current_profit = int(row[1])  # Set value for current profit to correct column
        change = current_profit - previous_profit  # Find difference in profit between rows
        changes.append(change) # Add new value to list of changes        
        current_date = row[0] # Set date for Max/Min profit as current row to correct column        

        if change > max_increase: # Set max_increase as current row if it is the greatest value so far
            max_increase = change
            max_increase_date = current_date # Save date of row with greatest value so far

        if change < max_decrease: # Set max_decrease as current row if it is the lowest value so far
            max_decrease = change
            max_decrease_date = current_date # Save date of row with lowest value so far

        previous_profit = current_profit # Update previous profit for the next iteration

    average_change = sum(changes[1:]) / (len(changes) - 1)

print("Financial Analysis") # Print all requested values for text analysis
print("------------------------")
print(f'Total Months: {total_months}')
print(f'Total: ${net_total}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {max_increase_date} (${max_increase})')
print(f'Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})')

output_file = "financial_analysis.txt" # Create text file with analysis data
with open(output_file, 'w') as output:
    output.write("Financial Analysis\n")
    output.write("------------------------\n")
    output.write(f'Total Months: {total_months}\n')
    output.write(f'Total: ${net_total}\n')
    output.write(f'Average Change: ${average_change:.2f}\n')
    output.write(f'Greatest Increase in Profits: {max_increase_date} (${max_increase})\n')
    output.write(f'Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n')

print(f"Financial analysis has been exported to {output_file}") # Confirm writing of text file
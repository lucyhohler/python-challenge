# First we'll import the os module
import os
# Module for reading csv file
import csv
csvpath = os.path.join('budget_data.csv')
# Export a text file with the results
file_output = "results.txt"
output = ""

# Open the file and read csv
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvfile)
    # Variables
    total_months = 0
    total_amount = 0
    total_changes = 0
    prev_amount = 0
    greatest_increase_month = ''
    greatest_increase_amount = float('-inf')
    greatest_decrease_month = ''
    greatest_decrease_amount = float('inf')
    
    # Loops
    for row in csvreader:
        total_months += 1
        amount = float(row[1])
        total_amount += amount
        if total_months > 1:
            change = (amount - prev_amount)
            total_changes += change
            if change > greatest_increase_amount:
                greatest_increase_amount = change
                greatest_increase_month = row[0]
            if change < greatest_decrease_amount:
                greatest_decrease_amount = change
                greatest_decrease_month = row[0]

        prev_amount = amount

    csvfile.close()

    average_change = total_changes / (total_months - 1)
    output = "Financial Analysis\n" + \
            "----------------------------\n" + \
            f"Total Months: {total_months}\n" + \
            f"Total: ${total_amount:.2f}\n" + \
            f"Average  Change: ${average_change:.2f}\n" + \
            f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase_amount:.2f})\n" + \
            f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease_amount:.2f})\n"

    # Print results to the terminal
    print(output)

# Export a text file with the results
with open(file_output, 'w') as txt_file:
    txt_file.write(output)
    
    txt_file.close()
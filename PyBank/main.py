# Import the os module
# This will allow us to create file paths across operating systems
import os
import csv

# Module for reading CSV files
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

# Read CSV file
# with open (csvpath, 'r') as file_handler:
#   lines = file_handler.read ()
#   print(lines)
#   print(type(lines))
# 

with open(csvpath) as csvfile:
    
    #CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skip headers Date and Profit/Losses
    budget_header = next(csvreader)

    #Create a list for months, profit/losses, and a dictionary to store the budget data
    month_yr = list()
    profit_loss = list()
    month_result = dict()
    i = 0
    
    #Loop through the budget data file to store data in lists and dictionary
    for row in csvreader:
        month_yr.append(row[0])
        profit_loss.append(int(row[1]))
        if i == 0:
            month_result[0] = month_yr[i]
        else:
            month_result[profit_loss[i] - profit_loss[i-1]] = month_yr[i]
        i += 1

    

# Total Number of Months included in the budget dataset
# Create a list and then a len() for total months
#print(month_yr)
#print(profit_loss)
#print(month_result)

# Print Financial Analysis results in Terminal
print("Financial Analysis")
print('--------------------------------------------------------')
total_months = len(month_yr)
print("Total Months:  " + str(total_months))

# Total Profit / Losses in aggregate
total_profit_loss = sum(profit_loss)
print("Total Profit / Loss:  " + "$" + str(total_profit_loss))

# Average Change
average_change = round(sum(month_result)/(total_months - 1),2)
print("Average Change:  " + "$" + str(average_change))

# Greatest Increase in Profits
great_inc_profit = max(month_result)
great_inc_date = month_result.get(great_inc_profit)
print("Greatest Increase in Profits:  " + great_inc_date + "  (" + "$" + str(great_inc_profit) + ")")

# Greatest Decrease i.e. Losses
great_losses = min(month_result)
great_dec_date = month_result.get(great_losses)
print("Greatest Decrease in Profits:  " + great_dec_date + "  (" + "$" + str(great_losses) + ")")


# Specify the file to write to pybankresults.csv in Anaylsis folder
output_path = os.path.join("Analysis", "pybankresults.csv")

# Open the file using "write" mode.
with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['-------------------------------------------'])
    csvwriter.writerow(['Total Months:  ' + str(total_months)])
    csvwriter.writerow(['Total Profit / Loss:  ' + '$' + str(total_profit_loss)])
    csvwriter.writerow(['Average Change:  ' + '$' + str(average_change)])
    csvwriter.writerow(['Greatest Increase in Profits:  ' + great_inc_date + '  (' +'$' + str(great_inc_profit) + ')'])
    csvwriter.writerow(['Greatest Decrease in Profits:  ' + great_dec_date + '  (' +'$' + str(great_losses) +')'])



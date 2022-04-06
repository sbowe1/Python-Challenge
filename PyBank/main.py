import os 
import csv

budget_path = os.path.join('Resources', 'budget_data.csv')
with open(budget_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Setting initial values
    total = 0
    prof_loss = []
    change = []
    greatest_inc = 0
    greatest_dec = 0
    total_months = 0
    
    # For loop to go through each row in the file
    for row in csvreader:
        # Adding the second value of the row to the total 
        total += int(row[1])
        # Turning column 2 into an array 
        prof_loss.append(int(row[1]))
        # Incrementing the total number of months each iteration
        total_months += 1

        current = int(row[1])
        # Greatest increase in profits (date and amount) over entire period
        # if profit is greater than previous greatest increase:        
        if current >= 0:
            if current > greatest_inc:
                greatest_inc = current # Save current value as the greatest increase
                greatest_inc_date = row[0] # Save the corresponding date 
        # Greatest decrease in profits (date and amount) over entire period
        # if losses exceed the previous greatest decrease:
        elif current < 0:
            if current < greatest_dec:
                greatest_dec = current # Save current value as greatest decrease
                greatest_dec_date = row[0] # Save the corresponding date
    
    # Changes in "Profit/Losses" over the period
    for i in range(len(prof_loss) - 1):
        change.append(prof_loss[i+1] - prof_loss[i])
    # Average of changes in "Profit/Losses"
    avg_change = round(((sum(change))/total_months), 2)
    
    # Print results
    print("Financial Analysis")
    print("----------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${avg_change}")
    print(f"Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc})")
    print(f"Greatest Decrease in Profits: {greatest_dec_date} (${greatest_dec})")
    
# Creating directory path for the output data
output_path = os.path.join('Analysis', 'PyBank.txt')

with open(output_path, 'w') as output:
    # The data to be printed
    text = (
        "Financial Analysis\n"
        "----------------------\n"
        f"Total Months: {total_months}\n"
        f"Total: ${total}\n"
        f"Average Change: ${avg_change}\n"
        f"Greatest Increase in Profits: {greatest_inc_date} (${greatest_inc})\n"
        f"Greatest Decrease in Profits: {greatest_dec_date} (${greatest_dec})\n"
    )
    
    # Adding the data to the txt file
    output.write(text)
    
    print(output)
import csv
import os
# Path to the CSV file
csv_path = os.path.join("Resources", "budget_data.csv")
ANALYSIS_PATH = os.path.join("analysis", "financial_analysis.txt")
# srart up  variables
total_months = 0
net_total = 0
changes = []
previousmonth_value = None
greatest_increase = {"Date": "", "Amount": 0}
greatest_decrease = {"Date": "", "Amount": 0}

# Open and read the CSV file
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(csv_path) as budget_data:
    csv_reader = csv.reader(budget_data)
    
    # Skip the header row
    header = next(csv_reader)
    
    # Loop through the file
    for row in csv_reader:
        # Increment the total number of months
        total_months += 1
        
        # net total amount of profit/loss over the entire time
        net_total += int(row[1])
        
        # Calculate the change from the previous month
        if previousmonth_value is not None:
            change = int(row[1]) - previousmonth_value
            changes.append(change)
            
            # Check if this change is the greatest increase or greatest decrease
            if change > greatest_increase["Amount"]:
                greatest_increase["Date"] = row[0]
                greatest_increase["Amount"] = change
            elif change < greatest_decrease["Amount"]:
                greatest_decrease["Date"] = row[0]
                greatest_decrease["Amount"] = change
        
        # Set the previous value for the next iteration
        previousmonth_value = int(row[1])

# Calculate the average change
average_change = sum(changes) / len(changes)

# Print the analysis to the terminal
print("financial Analysis")
print("------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_total}")
print(f"Average Change: ${round(average_change,2)}")
print(f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Amount']})")
print(f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Amount']})")

# Export the analysis to a text file
with open(ANALYSIS_PATH, "w") as file:
    file.write(f"financial Analysis\n")
    file.write(f"------------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${net_total}\n")
    file.write(f"Average Change: ${round(average_change,2)}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase['Date']} (${greatest_increase['Amount']})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease['Date']} (${greatest_decrease['Amount']})\n")

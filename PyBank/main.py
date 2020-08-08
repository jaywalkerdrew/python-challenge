import csv
import os

financeInput = os.path.join("Resources", "budget_data.csv")
financeOutput = os.path.join("analysis", "analysis.txt")

# initialize variables
totalMonths = 0
total = 0
previousProfit = 0.00
monthlyChange = []
greatestInc = 0
greatestDec = 0

# open CSV for read
with open(financeInput) as csvFile:
    reader = csv.reader(csvFile)
    
    # skip the header row
    header = next(reader)
    
    # loop through each row/month of data
    for row in reader:
        
        # find our current profit/loss, make it an integer
        currentProfit = int(row[1])

        # update totals
        totalMonths = totalMonths + 1
        total = total + currentProfit
        
        # update current change in profit/loss and add to the list
        # 'if' avoids adding a change to the list during the first iteration 
        if totalMonths == 1:
            currentChange = 0
        
        # update as usual otherwise    
        else:
            currentChange = currentProfit - previousProfit
            monthlyChange.append(currentChange)
        
        # assign the current month as previous for the next loop
        previousProfit = currentProfit

        # compare change to greatest change increase
        if currentChange > greatestInc:
            greatestInc = currentChange
            greatestIncMonth = row[0]
        # otherwise compare change to greatest change decrease
        elif currentChange < greatestDec:
            greatestDec = currentChange
            greatestDecMonth = row[0]

#calculate the average change and round to two decimals
averageChange = round(sum(monthlyChange) / len(monthlyChange), 2)

# print the financial results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${total}")
print(f"Average Change: ${averageChange}")
print(f"Greatest Increase in Profits: {greatestIncMonth} (${greatestInc})")
print(f"Greatest Decrease in Profits: {greatestDecMonth} (${greatestDec})")

# output to a text file
with open(financeOutput, "w") as out:
    out.write("Financial Analysis\n")
    out.write("----------------------------\n")
    out.write(f"Total Months: {totalMonths}\n")
    out.write(f"Total: ${total}\n")
    out.write(f"Average Change: ${averageChange}\n")
    out.write(f"Greatest Increase in Profits: {greatestIncMonth} (${greatestInc})\n")
    out.write(f"Greatest Decrease in Profits: {greatestDecMonth} (${greatestDec})\n")
out.close()        

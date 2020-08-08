import csv
import os

financeInput = os.path.join("Resources", "budget_data.csv")
financeOutput = os.path.join("analysis", "analysis.txt")

totalMonths = 0
total = 0
previousMonth = 0.00
monthlyChange = []
greatestInc = 0
greatestDec = 0

# open CSV for read
with open(financeInput) as csvFile:
    reader = csv.reader(csvFile)
    # skip the header row
    next(reader)

    for row in reader:
        currentMonth = int(row[1])

        totalMonths = totalMonths + 1
        total = total + currentMonth
        monthlyChange.append(currentMonth - previousMonth)

        if currentMonth > greatestInc:
            greatestInc = currentMonth
            greatestIncMonth = row[0]

        elif currentMonth < greatestDec:
            greatestDec = currentMonth
            greatestDecMonth = row[0]

        previousMonth = currentMonth

print(totalMonths)
print(total)



        

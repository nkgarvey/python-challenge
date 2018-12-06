#import the budget csv
import csv
Budget_csv ="C:/GitHub/python-challenge/pybank/Budget_csv.csv"
#create lists to store data
Total_Months = 0
Total_Profit = 0
Monthly_Change = 0
Greatest_Increase = 0
Greatest_Decrease = 0
previous_month = 0
Average_Change = 0
Month_Switch = []
#read in the file
with open(Budget_csv, newline = "", encoding = 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    #print(header)
#determine monthly change
    for row in csv.reader:
        if Total_Months == 0
        previous_month = float(row[1])
        else:
            Monthly_Change.append(float(row[1]) - previous_month)
            previous_month = float(row[1])
            Month_Switch.append (row[0])
    Total_Months = TotalMonths + 1
    Total_Profit = Total_Profit + 1
    # determine average monthly change
    Average_Change = (Monthly_Change) / 43
#find max and min monthly change
    for row in rows
     if Monthly_Change > 0
        Greatest_Increase = Monthly_Change.max
    else if Monthly_Change < 0
        Greatest_Decrease = Monthly_Change.min
  
      


print("Financial Analysis")
print("-----------------------------")
print("Total Months:" + Total_Months)
print("Total Profit:" + Total_Profit)
print("Average Change:" + Average_Change)
print("Greatest Profit Increase:" + Greatest_Increase)
print("Greatest Profit Decrease:" + Greatest_Decrease)


output_file = "C:/Users/nkgar/OneDrive/Documents/GitHub/python-challenge/pybank/Budget.new_txt.txt"







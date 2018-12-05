#import the budget csv
import csv
Budget_csv ="C:/Users/nkgar/OneDrive/Documents/GitHub/python-challenge/pybank/Budget_csv.csv"
#create lists to store data
TotalMonths = 0
ProfitLoss = []
Monthly_Change = []
Greatest_Increase = []
Greatest_Decrease = []
#read in the file
with open(Budget_csv, newline = "", encoding = 'utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    header = next(csvreader)
    print(header)
#count total month by len of Date column
#for row in csv.reader:
    for row in Budget_csv:
        #TotalMonths = 0
    #for row in rows:
        #TotalMonths = 0
        TotalMonths = int(TotalMonths) + int(row[1])
        print(TotalMonths)
        
# total net Profit/loss sum of ProfitLoss column
        ProfitLoss = 0
    #for row in rows:   
        #ProfitLoss += int(row[1])
# Monthly_Change in profit/loss. Need to create list of values based on (row + (row + 1)), then sum (those values)/43
        Monthly_Change = 0
    #remove the for loops, everything needs to be in one loop
    #for row in rows:
        Monthly_Change = sum(row[1] + (row[1] + 1)) / 43

# greatest increase = max value of sum(row +(row + 1)) if >0
#print("row + 1" + max)
# greatest decrease = min value of sum(row + (row + 1)) if <0
#print("row + 1" + min)
print("Financial Analysis")
print("-----------------------------")
print("Total Months:" + TotalMonths)
print("Profit/Loss:" + ProfitLoss)
print("Average Change:" + Monthly_Change)
print("Greatest Profit Increase:" + Greatest_Increase)
print("Greatest Profit Decrease:" + Greatest_Decrease)


output_file = "C:/Users/nkgar/OneDrive/Documents/GitHub/python-challenge/pybank/Budget.new_txt.txt"









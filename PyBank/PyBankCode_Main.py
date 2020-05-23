#Import dependencies

import os
import csv

#Point to reader file to import
bank_read_file = os.path.join('Resources/budget_data.csv')

#Create Lists to populate from bank file
month = []
net = []

#zip two lists to print in output file
zipped_output = zip(month, net)

#initialize read file, using encoding="utf8"
#naming file handle as web_starter_file

with open(bank_read_file, encoding="utf8") as bank_data:
    bankreader = csv.reader(bank_data, delimiter=',')
    bank_header = next(bankreader)


#Creating variables to store data to be printed on output folder
    highest_net = float(0)
    lowest_net = float(0)
    lowest_date = "a"
    highest_date = "b"

    for data in bankreader:
#Creating one list for each column for ease of evaluation
        month.append(data[0])
        net.append(data[1])
#Calculating highest and lowest values
        if ((float(data[1])) > highest_net):
            highest_net = float(data[1])
            highest_date = data[0]
        if ((float(data[1])) < lowest_net):
            lowest_net = float(data[1])
            lowest_date = data[0]

#Calculates Net Profit/Loss of the list
    profits = float(0)
    for x in net:
        profits = profits + float(x)

#Calculates # of Months in list
    month_count = len(month)

#Average Change
    avg_change = (float(profits)) / float(len(month))

#OUTPUT TO TERMINAL
    print("\n")
    print("=======================")
    print("Financial Analysis")
    print("=======================")
    print(f'Total Number of Months: {len(month)}')
    print(f'Total: ${format(profits,",.2f")}')
    print(f'Average Change: ${format(avg_change,",.2f")}')
    print(f'Greatest increase in profits: {highest_date}  ${format(highest_net,",.2f")}')
    print(f'Greatest increase in losses: {lowest_date}  ${format(lowest_net,",.2f")}')
    print("\n")

    output_stats = [month_count, profits, avg_change, highest_net, highest_net, lowest_date, lowest_net]

#OUTPUT TO FILE

bank_write_file = os.path.join('Analysis/BankPy_Output_File.txt')
with open(bank_write_file,'w',newline="") as output_data:
    bankwriter = csv.writer(output_data)
    bankwriter.writerow(["======================="])
    bankwriter.writerow(["Financial Analysis"])
    bankwriter.writerow(["======================="])
    bankwriter.writerow([f'Total Number of Months: {len(month)}'])
    bankwriter.writerow([f'Total: ${format(profits,",.2f")}']) 
    bankwriter.writerow([f'Average Change: ${format(avg_change,",.2f")}'])
    bankwriter.writerow([f'Greatest increase in profits: {highest_date}  ${format(highest_net,",.2f")}'])
    bankwriter.writerow([f'Greatest increase in losses: {lowest_date}  ${format(lowest_net,",.2f")}'])
    # bankwriter.writerow([])
    # bankwriter.writerow(["MONTH", "PROFIT/LOSS"])
    #bankwriter.writerows(zipped_output)

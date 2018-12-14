#PyBank Challenge

import os
import csv

budget_data_csv = os.path.join("..", "budget_data.csv")
months = []
total_PNL = 0
avg_PNL = 0
pnl_list = []
greatest_increase = 0
greatest_decrease = 0

with open(budget_data_csv, 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        months.append(row[0])
        pnl_list.append(int(row[1]))

total_months = len(months)                           
total_PNL = (sum(pnl_list))
pnl_pairs = list(zip(pnl_list, pnl_list[1:]))
pnl_diffs = [x[1] - x[0] for x in pnl_pairs]
avg_pnl_change = round((sum(pnl_diffs) / (len(pnl_diffs))),2)
greatest_increase = (max(pnl_diffs))
greatest_decrease = (min(pnl_diffs))

max_month = months[pnl_diffs.index(max(pnl_diffs)) + 1]  
min_month = months[pnl_diffs.index(min(pnl_diffs)) + 1]  

with open('output_PyBank.txt', 'w') as f:

    f.write("                       /n")
    f.write("Financial Analysis /n")
    f.write("-------------------- /n")
    f.write(f"Total months: {total_months} /n")
    f.write(f"Total: {total_PNL} /n")
    f.write(f"Average Change: {avg_pnl_change} /n")
    f.write(f"Greatest Increase in Profits: {max_month} ({greatest_increase}) /n")
    f.write(f"Greatest Decrease in Profits: {min_month} ({greatest_decrease}) /n")
    f.write("                       /n")



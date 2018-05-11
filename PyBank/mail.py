import os
import csv

csvpath = os.path.join('.', 'resources', "budget_data_1.csv")

#print(csvpath)

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    #print(csvfile)

    rev = []
    
    for row in csvreader:
        rev.append(row[1])
        
       
    # print(rev)
    # print(len(rev))

    i = len(rev)
    # print(rev[1:i])
    rev_2 = rev[1:i]
    rev_nums = [int(revenue) for revenue in rev_2]
    # print(rev_2)
    # print(rev_nums)
    tot_rev = sum(rev_nums)
    print('Total Months : ' + str(i - 1))
    print('Total Revenue : ' + str(tot_rev))
    
    # print(rev_nums[1])
dict_rev = {
    'month_rev' : rev_nums
}
    # print(dict_rev['month_rev'][0]) 
length = len(rev_nums)

change = []   
for k in range(length - 1):
    avg_change = (dict_rev['month_rev'][k + 1] - dict_rev['month_rev'][k])/ dict_rev['month_rev'][k]
    change.append(avg_change)
    
# print(change)

average_monthly_ch = sum(change) / (length-1)
print('Average Revenue Change : ' + str(average_monthly_ch))

incr_greatest = max(change)
print('Greatest Increase : ' + str(incr_greatest))

decr_greatest = min(change)
print('Greatest Decrease : ' + str(decr_greatest))

    
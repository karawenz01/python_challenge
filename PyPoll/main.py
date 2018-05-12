
import os
import csv
csvpath = os.path.join('.', "election_data_1.csv")

# print(csvpath)

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ',')
    

    candidate = []
    for row in csvreader:
        # print(row[2])
        candidate.append(row[2])
    
        
    i = len(candidate)
    can_votes = candidate[1:i]
        # print(can_votes)
    
    vestal_count = 0
    seth_count = 0
    torres_count = 0 
    cordin_count = 0

    for k in candidate:
        if k == 'Vestal':
            vestal_count = vestal_count + 1
        elif k == 'Seth':
            seth_count = seth_count + 1
        elif k == 'Torres':
            torres_count = torres_count + 1
        elif k == 'Cordin':
            cordin_count = cordin_count + 1

    tot_votes = vestal_count + seth_count + torres_count + cordin_count 
    print('Total Votes: ' + str(tot_votes))

    print('Vestal: '  + str((vestal_count / tot_votes)*100) + ' %' + ' (' + str(vestal_count) + ')' )
    
    print('Seth: '  + str((seth_count / tot_votes)*100) + ' %' + ' (' + str(seth_count) + ')' )

    print('Torres: '  + str((torres_count / tot_votes)*100) + ' %' + ' (' + str(torres_count) + ')' )

    print('Cordin: '  + str((cordin_count / tot_votes)*100) + ' %' + ' (' + str(cordin_count) + ')' )

    list_votes = [vestal_count, seth_count, torres_count, cordin_count]

    winner = max(list_votes)
    if vestal_count == winner:
        print('Winner: Vestal')
    elif seth_count == winner:
        print('Winner: Seth')
    elif torres_count == winner:
        print('Winner: Torres')
    elif cordin_count == winner:
        print('Winner: Cordin')


'''
    for k in candidate:
        if k == 'Khan':
            khan_count = khan_count + 1
        elif k == 'O'Tooley:
            otooley_count = otooley_count + 1
        elif k == 'Correy':
            correy_count = correy_count + 1
        elif k == 'Li':
            li_count = li_count + 1

    tot_votes = khan_count + otooley_count + correy_count + li_count
    print('Total Votes: ' + str(tot_votes))

    print('Khan: '  + str((khan_count / tot_votes)*100) + ' %' + ' (' + str(khan_count) + ')' )
    print('O'tooley: '  + str((otooley_count / tot_votes)*100) + ' %' + ' (' + str(otooley_count) + ')' )
    print('Correy: '  + str((correy_count / tot_votes)*100) + ' %' + ' (' + str(correy_count) + ')' )
    print('Li: '  + str((li_count / tot_votes)*100) + ' %' + ' (' + str(li_count) + ')' )

    list_votes = [khan_count, otooley_count, correy_count, li_count]

    winner = max(list_votes)
    if khan_count == winner:
        print('Winner: Khan')
    elif otooley_count == winner:
        print('Winner: O'tooley)
    elif correy_count == winner:
        print('Winner: Correy')
    elif li_count == winner:
        print('Winner: Li')
'''  
        
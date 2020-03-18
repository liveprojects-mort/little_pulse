import csv

with open('mycsv.csv', 'w', newline='') as f:    #'w' stands for WRITE
    theWriter = csv.writer(f)

    theWriter.writerow(['col1','col2','col3'])
    for i in range (5):
        theWriter.writerow(['one','two','three'])

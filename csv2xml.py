from asyncore import write
import csv
from ntpath import join


f = open('results.csv') #reading csv file
csv_f = csv.reader(f)
next(csv_f)
data = []

for row in csv_f:
    data.append(row) #storing row data as individual
f.close()

print(data[0:])

def convert_row(row):
    return """<testsuite name="%s" errors="%s" tests="%s" failures="%s" skipped="%s">
</testsuite>""" % (row[2], row[1], row[0], row[3], row[4])

with open('output.xml', 'w') as f:
        f.write('<?xml version="1.0"?>\n')
        f.write('<testsuites>\n')
        f.write('\n'.join([convert_row(row) for row in data]))
        f.write('\n</testsuites>')
"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import sys
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

distinct_numbers = set()

for entry in texts:
    distinct_numbers.update([entry[0], entry[1]])

for entry in calls:
    distinct_numbers.update([entry[0], entry[1]])

print('There are {} different telephone numbers in the records.'.format(len(distinct_numbers)))




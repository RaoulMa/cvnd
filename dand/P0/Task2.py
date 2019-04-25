"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
import sys
from datetime import datetime

def str_to_datetime(_str):
    return datetime.strptime(_str, '%d-%m-%Y %H:%M:%S')

def add_value(_dict, key, value):
    if key in _dict.keys():
        _dict[key] += value
    else:
        _dict[key] = value

# go through each entry and of 'calls'
time_dict = {}
for entry in calls:
    timestamp = str_to_datetime(entry[2])
    if timestamp.month == 9 and timestamp.year == 2016:
        add_value(time_dict, entry[0], int(entry[3]))
        add_value(time_dict, entry[1], int(entry[3]))

# compute maximum of time spent on the phone
max_value = -1
for key in time_dict.keys():
    if max_value < time_dict[key]:
        max_key = key
        max_value = time_dict[key]

# check for uniqueness
counter = 0
for value in time_dict.values():
    if max_value <= value:
        counter += 1
if counter > 1:
    print('Not unique')

print('{} spent the longest time, {} seconds, on the phone during September 2016'.format(max_key, time_dict[max_key]))




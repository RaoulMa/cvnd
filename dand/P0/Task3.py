"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

import sys

def get_prefix(_str):
    """ compute prefix: area code or mobile prefix """
    if ' ' in _str:
        return _str[:4]
    elif '(0' in _str and ')' in _str:
        left = _str.find('(')
        right = _str.find(')')
        return _str[left+1:right]
    elif '140' == _str[0:3]:
        return '140'
    else:
        print('Error: Telephone number can not be classified')

# Part A
_set = set()
for entry in calls:
    if '(080)' == entry[0][0:5]:
        _set.update([get_prefix(entry[1])])
_list = list(_set)
sorted_list = sorted(_list)
print("The numbers called by people in Bangalore have codes:")
for entry in sorted_list:
    print(entry)

# Part B
n_calls_from_Bangalore = 0
n_calls_from_Bangalore_to_Bangalore = 0
for entry in calls:
    if '(080)' == entry[0][0:5]:
        n_calls_from_Bangalore += 1
        if '(080)' == entry[1][0:5]:
            n_calls_from_Bangalore_to_Bangalore += 1
percentage = 100 * n_calls_from_Bangalore_to_Bangalore / n_calls_from_Bangalore
print('{:.2f} percent of calls from fixed lines in Bangalore are calls ' \
      'to other fixed lines in Bangalore.'.format(percentage))


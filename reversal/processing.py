"""
processing results from finance APIs
"""

import csv
import re
import numpy as np

# Google Finance API example
# https://www.google.com/finance/getprices?q=2330&x=TPE&i=3600&p=10d&f=d,c,h,l,o,v

def process_google_finance_history(gf_history_file):
    """
    Process a read stock history

    Args:
        gf_history_file: the path to the google finance history csv file

    Returns:
        A numpy array
    """

    interval = 86400
    timestamp = None
    current_timestamp = None
    processed = []

    for row in csv.reader(open(gf_history_file, 'r')):
        if len(row) is 0:
            continue
        if row[0].startswith('INTERVAL='):
            interval = int(row[0].split('INTERVAL=')[-1])
        if re.findall(r'^[a0-9]', row[0]):
            date = row[0]
            # absolute timestamp
            if date.startswith('a'):
                current_timestamp = timestamp = float(date.split('a')[-1])
            # relative offset
            else:
                offset = int(date)
                current_timestamp = timestamp + offset * interval
            row[0] = current_timestamp
            row[1:] = [float(value) for value in row[1:]]
            processed.append(row)
    return np.array(processed)

if __name__ == '__main__':

    process_google_finance_history('data/2330')

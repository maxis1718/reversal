import csv, re
import numpy as np
import matplotlib.pyplot as plt

# Google Finance API example
# https://www.google.com/finance/getprices?q=2330&x=TPE&i=3600&p=10d&f=d,c,h,l,o,v

def read_history (fn):
    '''
    @param str filename
    @return list parsed csv
    '''    
    return list(csv.reader(open(fn, 'r')))

def process (raw):
    '''
    @param list parsed csv
    '''
    interval = 86400
    timestamp = -1
    offset = 0
    for i in range(len(raw)):
        if len(raw[i]) is 0: continue
        if raw[i][0].startswith('INTERVAL='):
            interval = int(raw[i][0].split('INTERVAL=')[-1])
        # get time info
        if re.findall(r'^[a0-9]', raw[i][0]):
            _date, _close , _high, _low, _open, _volume = raw[i]
            # process date info
            if _date.startswith('a'):
                # starts with 'a', update absolute timestamp (1133933400.0)
                current_timestamp = timestamp = float(_date.split('a')[-1])
            else:
                # starts with number, in a relative format
                offset = int(_date)
                current_timestamp = timestamp + offset * interval
            ## update
            raw[i][0] = current_timestamp
            raw[i][1:] = list(map(float, raw[i][1:]))

    return np.array(raw)

def plot (data):
    plt.plot(data[0], y)



if __name__ == '__main__':

    raw = read_history('2330')
    process(raw)





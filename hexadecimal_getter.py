
# script used to get random hexadecimal value.
# params: length - int (length of the hexadecimal).
#         amount - int (how many hex-dec values).
#         fullpath - string (full path to the file we want to write the hex-dec to).
# better to use this with a loop (for / while) to get multiple values.

import random

def getRandomHex(length):
    return ''.join([random.choice('0123456789ABCDEF') for x in range(length)])

def getMultiHex(length,amount):
    while(amount):
        print getRandomHex(length)
        amount -= 1

def writeHexDecToFile(length,amount,fullpath):
    with open(fullpath , 'w') as f1:
        while(amount):
            f1.write(getRandomHex(length)+'\n')
            amount -= 1
    

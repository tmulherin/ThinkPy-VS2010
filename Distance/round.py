#!c:\python\python.exe
"""
    Returns a tuple with the integer part and the fractional part.
    Fractional part could be none if an integer was requested
"""
from datetime import datetime

def rounder(decimals, integer_part, fractional_part):

    iPart = int(integer_part)
    fPart = str(fractional_part)
    retval = []

    #==> Randomly decide to round up from 5 or 6
    micro = datetime.now().microsecond
    if micro % 2 == 0:                   #-> round up when the digit is greater than 4
        rnum = 4
    else: rnum = 5                       #-> round up when the digit is greater than 5

    done = False
    while done == False:
        if decimals == 0 and len(fPart) == 0:
            return(iPart, None)
        if decimals == len(fPart) or decimals > len(fPart):
            fPart += '0' * (decimals - len(fPart))
            done = True
        else:
            digit = fPart[-1]
            if int(digit) > rnum:
                dPart = float('.' + fPart)
                adder = float('.' + '0' * (len(fPart) - 1) + str(10 - int(digit)))
                result = dPart + adder
                if result == 1.0:
                    iPart += 1
                fPart = str(result)[2:]
            else: fPart = fPart[:-1]

    return (str(iPart), fPart)

if __name__ == '__main__':
    print("Equals        :", rounder(2, 12, '25'))
    print("Greater than  :", rounder(3, 12, '5'))
    print("9999 Less than:", rounder(2, 12, '9999'))
    print("9899 Less than:", rounder(2, 12, '9899'))
    print("1234 Less than:", rounder(2, 12, '1234')) 
    print("Integer no rnd:", rounder(0, 12, '1234'))
    print("Integer round :", rounder(0, 12, '99'))



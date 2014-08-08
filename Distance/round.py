#!c:\python\python.exe
"""
    Returns a tuple with the integer part and the fractional part.
    Fractional part could be None if an integer was requested
"""
from datetime import datetime
from traceback import extract_tb
from sys import exc_info
import utilities

def andOne(fract_to_round, round_hurdle=4):
    rnd = str(fract_to_round)
    adder = 0

    if len(rnd) == 1 and int(rnd) > round_hurdle:
        adder = 1

    while len(rnd) > 1:
        lastDigit = int(rnd[-1]) 
        rnd = rnd[:-1]
        if lastDigit + adder > round_hurdle:
                adder = 1
        else: adder = 0

    if int(rnd) > round_hurdle: adder = 1 
    return adder

def rounder(integer_part, fractional_part, decimals):

#    print("decimals =",decimals,'\nint =', integer_part, '\nfract =', fractional_part)
#    input()
    if utilities.isNumeric(integer_part):
        iPart = int(integer_part)
    else: pass ##################### need to error trap non numeric parameter values

    if utilities.isNumeric(fractional_part):
        fPart = str(fractional_part)
    else: pass ##################### need to error trap non numeric parameter values
    
    if utilities.isNumeric(decimals):
        decs = int(decimals)
    else: pass ##################### need to error trap non numeric parameter values
    retval = []

    #==> Randomly decide to round up from 5 or 6
    micro = datetime.now().microsecond
    if micro % 2 == 0:                   #-> round up when the digit is greater than 4
        rnum = 4
    else: rnum = 5                       #-> round up when the digit is greater than 5

    done = False
    while not done:
        if decs == 0 and (len(fPart) == 0 or int(fPart) == 0):
            fPart = None
            break
        if decs == len(fPart) or decs > len(fPart):
            fPart = fPart + ('0' * (decs - len(fPart)))
            break
                            
        base = fPart[:decs]

        if __name__ == '__main__': print('\nRounding: iPart = %d; fPart = %s, decimals = %d, base = %s' % (iPart, fPart, decimals, base))

        adder = andOne(fPart[decs:], rnum)
          
        if adder == 1:
            if len(base) == 0:
                iPart += 1
                fPart = '0'
            else:
                while adder == 1 and len(base) > 1:
                    lastDigit = int(base[-1])
                    base = base[:-1]

                    if lastDigit < 9:
                        base = base + str(lastDigit + 1)
                        adder = 0

                if __name__ == '__main__': print('adder = %d, base = %s' % (adder, base))
                if len(base) == 1 and adder == 1:
                    if base[0] == '9':
                        iPart += 1
                        fPart = '0'
                    else: fPart = str(int(base) + 1)
                else:
                    fPart = base
        else:
            if len(base) == 0: fPart = '0'
            else: fPart = base        


    return (str(iPart), fPart)

if __name__ == '__main__':
    utilities.clearScreen(); print('\n\n')
    print("12.25    - 12.25  :", rounder(12, '25', 2))
    print('12.5     - 12.500 :', rounder(12, 5, 3))
    print("12.9999  - 13.00  :", rounder(12, '9999', 2))
    print("12.9899  - 12.99  :", rounder(12, '9899', 2))
    print("12.3434  - 12.34  :", rounder(12, '3444', 2))
    print("12.3496  - 12.35  :", rounder(12, '3496', 2))
    print("12.3444  - 12     :", rounder(12, '3444', 0))
    print("0.034166 -  0.03  :", rounder(0,  '034166', 2)) 
    print("12.99    - 13     :", rounder(12, '99', 0))
    print('2.596    - 2.60   :', rounder(2, 596, 2))
    print('0.099167 - 0.10   :', rounder(0, '099167', 2))


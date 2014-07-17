def andOne(fract_to_round, rnum=4):
    rnd = str(fract_to_round)
    adder = 0

    if len(rnd) == 1 and int(rnd) > rnum:
        adder = 1

    while len(rnd) > 1:
        lastDigit = int(rnd[-1]) 
        rnd = rnd[:-1]
        if lastDigit + adder > rnum:
                adder = 1
        else: adder = 0
    return adder

base, fPart, decs = '19', '9999', 2



print('12345; %d' % andOne('12345'))
print('99999; %d' % andOne('99999'))
print('9; %d' % andOne('9'))
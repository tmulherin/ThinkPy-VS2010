#!c:\python\python

import PopScreen

def formatNumber(value, number_of_decimal_places = 0, commas_desired = 0):

    #==> Check that the numeric inputs are valid
    if not isNumber(value):
        return "Error: " + str(value) + " is not a number"
    if not isNumber(number_of_decimal_places):
        return "Error: " + str(number_of_decimal_places) + " is not a number"
    if not isNumber(commas_desired):
        return "Error: commas = " + str("'" + commas_desired + "'") + "? commas must be either 0 (No) or not 0 (Yes)"

#-------------------------------------------------------------------------------------------------

    i_dec_places    = int(number_of_decimal_places)
    i_commas        = int(commas_desired)

    number          = str(value)

    integer_part    = ""
    fractional_part = ""

    dec_loc = inStr(number, ".")
    print("dec_loc = " + str(dec_loc))


    if dec_loc == -1:
        integer_part = number
    elif dec_loc == 0:
        integer_part = "0"
        fractional_part = number[1:]
    else:
        integer_part    = number[:dec_loc]
        fractional_part = number[dec_loc + 1:]

    print("i_dec_places = " + str(i_dec_places))

#-------------------------------------------------------------------------------------------------

    diff = i_dec_places - len(fractional_part)

    if i_dec_places > 0 and diff > -1: number += '0' * diff

    if i_dec_places > 0 and diff < 0:
        fracts_to_keep = fractional_part[:diff]
        if fracts_to_keep[-1] != '9': #--> only round if last keeper is less than 9
            fracts_to_round = fractional_part[diff:]
            if len(fracts_to_round) > 1:
                fracts_to_round = roundFractionalsToOne(fracts_to_round)
            if int(fracts_to_round) > 4:
                fracts_to_keep = str(int(fracts_to_keep) + 1)

        number = (integer_part + '.' + fracts_to_keep)

    if i_dec_places == 0:
        if len(fractional_part) > 0:
            test_dec = roundFractionalsToOne(fractional_part)
            #print("n = " + number, "t =" + test_dec, "i = " + integer_part, "f =" + fractional_part)
            if int(test_dec) > 4: integer_part = str(int(integer_part) + 1)
        number = integer_part

    if i_commas:
        integer_part = "0"
        fractional_part = "0"
        dec_loc = inStr(number, ".")

        if dec_loc == -1:
            integer_part = number
        elif dec_loc == 0:
            integer_part = "0"
            fractional_part = number[1:]
        else:
            integer_part = number[:dec_loc]
            fractional_part = number[dec_loc + 1:]

        if len(integer_part) > 3:
            commad = ""
            templist = list(integer_part)
            templist.reverse()
            integer_part = listToString(templist)
            while len(integer_part) > 3:
                commad += integer_part[0:3] + ','
                integer_part = integer_part[3:]
            commad += integer_part
            templist = list(commad)
            templist.reverse()
            integer_part = listToString(templist)

        if dec_loc == -1:
            number = integer_part
        else:
            number =  integer_part + '.' + fractional_part

    return number    

def IsInt(value):
    if isNumber(value):
        if float(value) % int(value) == 0.0:
            return 1

    return 0

def isNumber(string):

    string = str(string) #-> Just in case...
    decimal_counter = 0

    for char in string:
        if char == ".":
            decimal_counter += 1
            if decimal_counter > 1:
                return 0
        elif char not in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            return 0

    return 1

def inStr(string, substring):
    "Reminder: the caller must check for a return value of -1 (not found)"
    loc = -1 #--> Because Python starts counting at zero, search_string
#                 could be at the zeroth position.  Bah!

    string = str(string) #--> In case it ain't a string!
    substring = str(substring) #--> Ditto

#    print('string = ' + string + ", substring = " + substring)
    for char in string:
        loc += 1 # Starts us off at position zero
        if char == substring[0] and substring == string[loc:loc + len(substring)]:
            return loc

    return -1 # substring not in string

def roundFractionalsToOne(fractionals):
    fractionals = str(fractionals)
    if len(fractionals) > 1:
        if int(fractionals[0]) < 9:
            while len(fractionals) > 2:
                lastDigit = int(fractionals[-1])
                if lastDigit > 4:
                    fractionals = str(int(fractionals) + 10 - lastDigit)
                fractionals = fractionals[:len(fractionals) - 1]
            if int(fractionals[0]) < 9 and int(fractionals[1]) < 4:
                fractionals = int(fractionals[0]) + 1

    return fractionals

def listToString(some_list):
    retVal = ""
    for char in some_list:
        retVal += str(char)

    return retVal

if __name__ == '__main__':
    pass
#!c:\python\python

import round
import os
import parse_time

def clearScreen():
    os.system("cls")

def format_number(value, number_of_decimal_places = 0, commas_desired = 0):

    #==> Check that the numeric inputs are valid
    if not isNumeric(value):
        return "Error: " + str(value) + " is not a number"
    if not isNumeric(number_of_decimal_places):
        return "Error: " + str(number_of_decimal_places) + " is not a number"
    if not isNumeric(commas_desired):
        return "Error: commas = " + str("'" + commas_desired + "'") + "? commas must be either 0 (No) or not 0 (Yes)"

#-------------------------------------------------------------------------------------------------

    i_dec_places    = int(number_of_decimal_places)

    i_commas        = int(commas_desired)

    number          = str(value)

    integer_part    = ""
    fractional_part = ""

    dec_loc = inString(number, ".")
#    print("dec_loc = " + str(dec_loc))

    if dec_loc == -1:
        integer_part = number
        fractional_part = '0'
    elif dec_loc == 0:
        integer_part = "0"
        fractional_part = number[1:]
    else:
        integer_part    = number[:dec_loc]
        fractional_part = number[dec_loc + 1:]

    number = round.rounder(i_dec_places, integer_part, fractional_part)
    integer_part = number[0]
    fractional_part = number[1]
#------------------------------------------------------------------------ Have to make this reflect integers ------------------------
    if i_commas:
        if len(integer_part) > 3:
            commad = ""
            templist = list(integer_part)
            templist.reverse()
            integer_part = list_to_string(templist)
            while len(integer_part) > 3:
                commad += integer_part[0:3] + ','
                integer_part = integer_part[3:]
            commad += integer_part
            templist = list(commad)
            templist.reverse()
            integer_part = list_to_string(templist)

        if dec_loc == -1:
            number = integer_part
        else:
            number =  integer_part + '.' + fractional_part

    return number    

def getopts(argv):
    opts = []
    argv = argv[1:] #-> Strip out the first element: /home/tim/dev/ProgPy4/03_ScriptExec/testargv.py'
    while len(argv) > 0:
        if argv[0][0] == '-':
            opts.append(argv[0])
        if len(argv) > 1:
            argv = argv[1:]
        else: argv = []
      
    return opts

def inString(string, substring):
    """
        Returns -1 if the substring was not found
        else it returns the position of the substring 
    """
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

def isInt(value):
    try:
        aString = str(value)
        if (type(eval(aString)) is int) is True:
            return True
        else: return False
    except:
        return False

def isFloat(value):
    try:
        aString = str(value)
        if (type(eval(aString)) is float) is True:
            return True
        else: return False
    except:
        return False

def isNumeric(value):
    aString = str(value)
    theNum = aString.split('.')
    
    try:
        aString = str(int(theNum[0]))
        for char in theNum[1:]:
            aString += ('.' + char)
    except:
        pass

    if isInt(aString) or isFloat(aString):
        return True
    else: return False

def list_to_string(some_list):
    retVal = ""
    for char in some_list:
        retVal += str(char)

    return retVal

def parseTime(time_string, sep = ':'):
    """
    String should be in the form of (days:hours:minutes:seconds)
    This reverses the string so that seconds are evaluated first
        followed by minutes then hours, etc until the strings length is 
        reduced to 0.      
    """
    seconds = 0.0
    string = reverseString(time_string)    #-> Reversed string sss:mmm:hhh:ddd:yyy

    #==> get seconds
    trial = stripString(string, sep)
    if __name__ == '__main__': print("Seconds = " + trial[1])
    if isNumeric(trial[1]):
        seconds += float(trial[1])
        if not trial[2] is None:
    #==> get minutes
            trial = stripString(trial[2], sep)
            if __name__ == '__main__': print("Minutes = " + trial[1])
            if isNumeric(trial[1]):
                seconds += float(trial[1]) * 60.0 
                if not trial[2] is None:
    #--> get hours
                    trial = stripString(trial[2], sep)
                    if __name__ == '__main__': print("Hours   = " + trial[1])
                    if isNumeric(trial[1]):
                        seconds += float(trial[1]) * 60.0 * 60.0
    #--> get days
                        if not trial[2] is None:
                            trial = stripString(trial[2], sep)
                            if __name__ == '__main__': print("Days    = " + trial[1])
                            if isNumeric(trial[1]):
                                seconds += float(trial[1]) * 24.0 * 60.0 * 60.0
                            else: return ("Error   = '%s' is not a valid number of days!" % str(trial[1]))
                    else: return ("Error   = '%s' is not a valid number of hours!" % str(trial[1]))
            else: return ("Error   = '%s' is not a valid number of minutes!" % str(trial[1]))
    else: return ("Error   = '%s' is not a valid number of seconds!" % str(trial[1]))

    return seconds

def reverseString(a_string):
    result = []
    for char in str(a_string):
        result.append(char)
    result.reverse()
    return list_to_string(result)

def stripString(string, separator=','):
    """ 
        Input
        -----
        delimited string
        separator value
        
        Output ret_val[0, 1, 2]
        -------------
        0: Location of the separator
        1: 0th character up to the character preceding the separator
        2: Remainder of the string
    """

    ret_val = [0, '', '']
    ret_val[0] = inString(string, separator)
#    print('separator =', separator_location)
    if ret_val[0] == -1:                      #--> No more delimiters!
        if len(string) > 0:
            ret_val[1] = reverseString(string)
            ret_val[2] = None
#        print("string is " + string + " in stripString")
#        ret_val = [separator_location, string, None]    
    elif ret_val[0] == 0:                     #-----------------------------------------------> Oops 
        pass
    else:
        ret_val[1] = reverseString(string[:ret_val[0]])
        string = string[ret_val[0]:]
        if len(string) > len(separator):
            ret_val[2] = (string[len(separator):])
        else:                                            #--> Done - ended on a delimiter!
            ret_val[2] = (None)
#    print(ret_val)    
    return ret_val

def testTime():
        tests = []
        def test(string):
            result = parseTime(string)
            print("Input   = " + string)
            if isNumeric(str(result)):
                print("Total   = " + format_number(str(result), 2, 1))
            else: print(result)
            if isNumeric(str(result)):
                print("Time    = " + format_number(str(result/60/60), 2, 1), '\n')
            else: print()
       
        clear_screen()
        tests.append('3:3:3')
        tests.append('3')
        tests.append('10:30:30')
        tests.append('100:450:70000')
        tests.append('26:19:26:0')
        tests.append('.5:.5:.5:.5')
        tests.append('Fred')
        tests.append('Ethyl:.5')
        tests.append('Ricky:.5:.5')
        tests.append('Lucy:.5:.5:.5')
        tests.append('')

        for aTest in tests:
            test(aTest)

if __name__ == '__main__':
    from sys import argv
    myArgs = getopts(argv)
    for process in myArgs:
        if process == '-time':
                testTime()


#    clear_screen(); print('No tests selected')
#    testTime()

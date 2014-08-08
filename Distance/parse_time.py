#!c:\python\python

import utilities

def reverseString(a_string):
    result = []
    for char in str(a_string):
        result.append(char)
    result.reverse()
    return utilities.list_to_string(result)

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
    ret_val[0] = utilities.inString(string, separator)
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
    if utilities.isNumeric(trial[1]):
        seconds += float(trial[1])
        if not trial[2] is None:
    #==> get minutes
            trial = stripString(trial[2], sep)
            if __name__ == '__main__': print("Minutes = " + trial[1])
            if utilities.isNumeric(trial[1]):
                seconds += float(trial[1]) * 60.0 
                if not trial[2] is None:
    #--> get hours
                    trial = stripString(trial[2], sep)
                    if __name__ == '__main__': print("Hours   = " + trial[1])
                    if utilities.isNumeric(trial[1]):
                        seconds += float(trial[1]) * 60.0 * 60.0
    #--> get days
                        if not trial[2] is None:
                            trial = stripString(trial[2], sep)
                            if __name__ == '__main__': print("Days    = " + trial[1])
                            if utilities.isNumeric(trial[1]):
                                seconds += float(trial[1]) * 24.0 * 60.0 * 60.0
                            else: return ("Error   = '%s' is not a valid number of days!" % str(trial[1]))
                    else: return ("Error   = '%s' is not a valid number of hours!" % str(trial[1]))
            else: return ("Error   = '%s' is not a valid number of minutes!" % str(trial[1]))
    else: return ("Error   = '%s' is not a valid number of seconds!" % str(trial[1]))

    return seconds
    
if __name__ == '__main__':
    def test(string):
        result = parseTime(string)
        print("Input   = " + string)
        if utilities.isNumeric(str(result)):
            print("Total   = " + utilities.format_number(str(result), 2, 1))
        else: print(result)
        if utilities.isNumeric(str(result)):
            print("Time    = " + utilities.format_number(str(result/60/60), 2, 1), '\n')
        else: print()
       
    utilities.clearScreen()
    test('3:3:3')
    test('3')
    test('10:30:30')
    test('100:450:70000')
    test('26:19:26:0')
    test('05:05')
    test('.5:.5:.5:.5')
    test('Fred')
    test('Ethyl:.5')
    test('Ricky:.5:.5')
    test('Lucy:.5:.5:.5')
    test('')
    test('12:0')

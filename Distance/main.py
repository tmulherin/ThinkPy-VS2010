#!c:\python\python

"""
--------------------------------
D:\__Dev\Python\ThinkPy\main.py
--------------------------------

cd D:\__Dev\Python\ThinkPy
cd /D/__Dev/Python/ThinkPy

"""
import utilities    
import os
#from decimal import Decimal

line_blank = "  :" + ' '*74 + ":"
line_dashed = "  :" + '-'*74 + ":"

pad = ' '*19

prompt_distance = "How far was the activity pursued? "
prompt_rate = "At what speed was the activity pursued? "
prompt_hours = "For how many hours was the activity pursued? "
prompt_minutes = "For how many minutes was the activity pursued? "
prompt_seconds = "For how many seconds was the activity pursued? "
prompt_info = "--> "
prompt_cont = "\nPress [Enter] to contimue"
result_set = []

title_distance = "  :" + " " * 29 + "<<< Distance >>>" + " " * 29 + ":"
title_rate = "  :" + " " * 31 + "<<< Rate >>>" + " " * 31 + ":  "
title_time = "  :" + " " * 31 + "<<< Time >>>" + " " * 31 + ":  "
title_cols = "  :" + " " * 12 + "Distance" + " " * 16 + "Rate" + " "* 16 + "Time" + " " * 14 + ":"
title_seps = "  :" + " " * 12 + "--------" + " " * 16 + "----" + " "* 16 + "----" + " " * 14 + ":"

distance = 0.0
rate = 0.0
time = 0.0

def cls():
    os.system("cls")
#    print("\x1B[2J")

def dummyProc(something):
    pass
    
def GetRate():
    got_rate = 0

    while not got_rate:
        rate = input(prompt_info + prompt_rate)
        if len(rate) > 0:
            if utilities.isNumber(rate):
                return float(rate)
            else:
                print(rate + " is not a valid rate of speed.  Press any key to continue.")
                rate = input()
        else:
            print("You must enter a valid number")

def GetSolutionType():

    tries = 0
    prompt = "Are you looking for [d]istance, [r]ate or [t]ime? \n  > "

    err_msg = " is not a valid Distance problem.  "


    fail_msg = "\n\n\n" + " "*30 + "Three strikes you're out!"
    strikes = ['One', 'Two', 'Three']
    while tries < 3:
        tries += 1
        cls()
        for i in range(30): print()
 
        sol_type = input(prompt)

        if len(sol_type) > 0:
            if sol_type.lower() in("distance", "rate", "time"):
                return sol_type[0].lower()
            elif sol_type.lower() in("d", "r", "t"):
                return sol_type.lower()
            else:
                err = "\n" + "'" + sol_type + "'" + " " + err_msg
                err += "That's Strike " + strikes[tries - 1]
                if tries < 3:
                    err = input(err + '\n' + prompt_cont)
                else:
                    err = input(err + " --> You're Out" )
        else:
            return 0 #empty input = quit

    return 0

def GetTime():

    got_time = 0
    thisTime = 0
    while not got_time:
        hours = input(prompt_info + prompt_hours)
        if len(hours) == 0:
            got_time = 1 
        else:
            if utilities.isNumber(hours):
                got_time = 1
                thisTime = int(hours)*60*60
            else:
                print(hours + " is not a valid number of hours.  Press any key to continue.")
                hours = input()

    got_time = 0
    while not got_time:
        minutes = input(prompt_info + prompt_minutes)
        if len(minutes) == 0:
            got_time = 1
        else:
            if utilities.isNumber(minutes):
                got_time = 1
                thisTime += int(minutes)*60
            else:
                print(minutes + " is not a valid number of minutes.  Press any key to continue.")
                minutes = input()

    got_time = 0
    while not got_time:
        seconds = input(prompt_info + prompt_seconds)
        if len(seconds) == 0:
            got_time = 1
        else:
            if utilities.isNumber(seconds):
                got_time = 1
                thisTime += int(seconds)
            else:
                print(seconds + " is not a valid number of minutes.  Press any key to continue.")
                seconds = input()

#thisTime = float(thisTime)/60/60
             
    return thisTime # = Total seconds
  
def PopScreen(title, output_line = []):
    cls()
    print()
    print(line_dashed)
    print(line_blank)
    print(title)
    print(line_blank)
    print(line_dashed)
    print(line_blank)
    print(title_cols)
    print(title_seps)
#   print("  :          1         2        3")
#   Print("  :0123456789012345678901234567890")

#############    trips = 0   


    # ==> Populate the matrix with the calculated info
    for i in result_set: # result_set is a list of lists...
        disp = (pad + str(i[0])[:14])
        disp += (pad + str(i[1])[:14])
        disp += (pad + str(i[2])[:14])
        disp += " "*14
        print("  :" + disp + ":")

    #==> Populate the matrix with the info we're working on:
    if len(output_line) > 0:
        disp = (pad + str(output_line[0]))[len(output_line[0]) - 1:]
        disp += (pad + str(output_line[1]))[len(str(output_line[1])) - 1:]
        disp += (pad + str(output_line[2]))[len(str(output_line[2])) - 1:]
        disp += " " * 14
        print("  :" + disp + ":")

    for i in range(29-len(result_set)):
        print(line_blank)

    print(line_dashed)
    print()

def SolutionForDistance():
    '''
        output_line[0] = distance
        output_line[1] = rate
        output_line[2] = time
    '''
    PopScreen(title_distance)

    output_line = ["?", "?", "?"] #--> Distance = Rate * Time
    rate = GetRate()
    output_line[1] = utilities.formatNumber(rate, 2, 1)

    PopScreen(title_distance, output_line)

    #Get_Time()
    #Calculate distance
    time = GetTime()
    output_line[2] = utilities.formatNumber(float(time)/60/60, 2, 1)
    output_line[0] = utilities.formatNumber(float(rate * time)/60/60, 2, 1)
    PopScreen(title_distance, output_line)
    input(prompt_info)

def SolutionForRate():
    PopScreen(title_rate)

def SolutionForTime():
    PopScreen(title_time)

def SolveProblem(sol_type):

    if sol_type == "d":
        SolutionForDistance()
    elif sol_type == "r":
        SolutionForRate()
    elif sol_type == "t":
        SolutionForTime()
    else:
        cls()
        quit()

def main():
    SolveProblem(GetSolutionType())

if __name__ == '__main__':
    main()

#!c:\python\python

"""
--------------------------------
D:\__Dev\Python\ThinkPy\main.py
--------------------------------

cd D:\__Dev\Python\ThinkPy
cd /D/__Dev/Python/ThinkPy

"""
import display
import utilities    
import os

#from decimal import Decimal

prompt_distance = "How far was the activity pursued? "
prompt_rate = "At what speed was the activity pursued? "
prompt_hours = "For how many hours was the activity pursued? "
prompt_minutes = "For how many minutes was the activity pursued? "
prompt_seconds = "For how many seconds was the activity pursued? "
prompt_info = "--> "
prompt_cont = "\nPress [Enter] to contimue"

distance = 0.0
rate = 0.0
time = 0.0

new_values = ['?', '?', '?']
result_set = []

def dummyProc(something):
    pass

def get_distance():
    done = 0
    while done == 0:
        distance = input(prompt_info + prompt_distance)
        if len(distance) > 0 and utilities.is_number(distance):
            return float(distance)
        else:
            print("You must enter a valid rate.  Press any key to continue.")

    
def get_rate():
    got_rate = 0

    while not got_rate:
        rate = input(prompt_info + prompt_rate)
        if len(rate) > 0:
            if utilities.is_number(rate):
                return float(rate)
            else:
                print(rate + " is not a valid rate of speed.  Press any key to continue.")
                rate = input()
        else:
            print("You must enter a valid number")

def get_solution_type():

    tries = 0
    prompt = "Are you looking for [d]istance, [r]ate or [t]ime? \n  > "
    err_msg = " is not a valid Distance problem.  "


    fail_msg = "\n\n\n" + " "*30 + "Three strikes you're out!"
    strikes = ['One', 'Two', 'Three']
    while tries < 3:
        display.clear_screen()
        tries += 1
        for i in range(30): print()
 
        sol = input(prompt)
        if len(sol) > 0:
            if sol.lower() in("distance", "rate", "time"):
                return sol[0].lower()
            elif sol.lower() in("d", "r", "t"):
                return sol.lower()
            else:
                err = "\n" + "'" + sol + "'" + " " + err_msg
                err += "That's Strike " + strikes[tries - 1]
                if tries < 3:
                    err = input(err + '\n' + prompt_cont)
                else:
                    err = input(err + " --> You're Out" )
        else:
            return 0 #empty input = quit

    return 0

def get_time():

    got_time = 0
    thisTime = 0
    while not got_time:
        hours = input(prompt_info + prompt_hours)
        if len(hours) == 0:
            got_time = 1 
        else:
            if utilities.is_number(hours):
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
            if utilities.is_number(minutes):
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
            if utilities.is_number(seconds):
                got_time = 1
                thisTime += int(seconds)
            else:
                print(seconds + " is not a valid number of minutes.  Press any key to continue.")
                seconds = input()

#thisTime = float(thisTime)/60/60
             
    return thisTime # = Total seconds
  
def solution_for_distance():
    '''
        output_line[0] = distance
        output_line[1] = rate
        output_line[2] = time
    '''
    result_set.append(new_values)
    display.pop_screen('d', result_set)

    rate = get_rate()
    result_set[-1][1] = utilities.format_number(rate, 2, 1)

    display.pop_screen('d', result_set)

    #Get_Time()
    #Calculate distance
    time = get_time()
    result_set[-1][2] = utilities.format_number(float(time)/60/60, 2, 1)
    result_set[-1][0] = utilities.format_number(float(rate * time)/60/60, 2, 1)
    display.pop_screen('d', result_set)
    input(prompt_info)

def solution_for_rate():
    '''
        output_line[0] = distance
        output_line[1] = rate
        output_line[2] = time
    '''
    result_set.append(new_values)
    display.pop_screen('r', result_set)

    distance = get_distance()
    result_set[-1][0] = utilities.format_number(distance, 2, 1)

    display.pop_screen('r', result_set)
    
    #Calculate distance
    time = get_time()
    result_set[-1][2] = utilities.format_number(float(time)/60/60, 2, 1)
    
    #==> Here's the meat:
    hours = time / 60 / 60
    result_set[-1][1] = utilities.format_number(float(distance / hours), 2, 1)
    
    display.pop_screen('r', result_set)
    input(prompt_info)
def solution_for_time():
    display.pop_screen(title_time)

def main():
    done = False
    sol_type = (get_solution_type())
    if sol_type == "d":
        solution_for_distance()
    elif sol_type == "r":
        solution_for_rate()
    elif sol_type == "t":
        solution_for_time()
    else:
        display.clear_screen()
        quit()

if __name__ == '__main__':
    main()

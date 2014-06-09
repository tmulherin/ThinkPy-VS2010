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

prompt_distance = "How far? "
prompt_rate = "How fast? "
prompt_time = "How long ([ddd.d]:[hhh.h]:[mmm.m]:sss.s)? "
prompt_info = "--> "
prompt_cont = "\nPress any key to contimue"

distance = 0.0
rate = 0.0
time = 0.0

new_values = ['?', '?']
result_set = []

def dummyProc(something):
    pass

def get_distance():
    done = 0
    while done == 0:
        distance = input(prompt_info + prompt_distance)
        if len(distance) > 0 and utilities.isNumeric(distance):
            return float(distance)
        else:
            print("You must enter a valid distance.  Press any key to continue.")
    
def get_rate():
    got_rate = 0

    while not got_rate:
        rate = input(prompt_info + prompt_rate)
        if len(rate) > 0:
            if utilities.isNumeric(rate):
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
        utilities.clearScreen()
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
    while 1:
        time_string = input(prompt_info + prompt_time)
        if len(time_string) > 0:
            seconds = utilities.parseTime(time_string, ':')
            if utilities.isNumeric(seconds):
                return seconds
            else:
                myErr = seconds      
        else:
            myErr = "You need to enter some time." 
        input(prompt_cont)
           
'''
    output_line[0] = distance
    output_line[1] = time
'''  
def solution_for_distance():

    result_set[-1][1] = get_time()
    display.pop_screen('d', result_set)

    result_set[-1][0] = get_rate() * result_set[-1][1]/60/60 
       
def solution_for_rate():

    result_set[-1][0] = get_distance()
    display.pop_screen('r', result_set)
    
    result_set[-1][1] = get_time()
    
def solution_for_time():

    result_set[-1][0] = get_distance()
    display.pop_screen('t', result_set)
    
    result_set[-1][1] = distance / get_rate()
    
def main():
    done = False
    result_set.append(new_values)
    sol_type = (get_solution_type())
    display.pop_screen(sol_type, result_set)
    if sol_type == "d":
        solution_for_distance()
    elif sol_type == "r":
        solution_for_rate()
    elif sol_type == "t":
        solution_for_time()
    else:
        quit()

    display.pop_screen(sol_type, result_set)
    input(prompt_info)

if __name__ == '__main__':
    main()

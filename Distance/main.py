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
from sys import argv

prompt_distance = "How far? "
prompt_rate = "How fast? "
prompt_time = "How long ([ddd.d]:[hhh.h]:[mmm.m]:sss.s)? "
prompt_info = "--> "
prompt_cont = "\nPress any key to continue"

distance = 0.0
rate = 0.0
time = 0.0
sol_types = {}
result_set = []

def delete(row):
    pass

def edit(row):
    pass

def get_distance():
    done = 0
    while done == 0:
        distance = input(prompt_info + prompt_distance)
        if len(distance) > 0 and utilities.isNumeric(distance):
            return float(distance)
        else:
            print("You must enter a valid distance.  Press any key to continue.")
    
def get_rate(solution_type):
    got_rate = 0

    while not got_rate:
        rate = input(prompt_info + prompt_rate)
        if len(rate) > 0:
            if utilities.isNumeric(rate):
                return float(rate)
            else:
                myErr = rate + " is not a valid rate of speed."
        else:
            myErr = "You must enter a valid number"
        if len(myErr) > 0:
            print(myErr)
            input(prompt_cont)
            display.pop_screen(solution_type, result_set)   

def get_intent():

    intents = {'s': 'solve problem', 'e': 'edit', 'd': 'delete', 'q': 'quit'}

    while True:

        if len(result_set) > 0:
            display.pop_screen(result_set)
        else:
            utilities.clearScreen()
            for i in range(51): print()
        print("""
 [s]olve an equation 
 [e]dit a row
 [d]elete a row
 [q]uit """)
        response = input('> ')

        if response.lower() in intents.keys() or response.lower() in intents.values():
            return intents[response[0].lower()]
        else:
            input("%s is not a valid intent.  Press any key to continue." % response)

def get_solution_type():

    prompt = "Are you looking for [d]istance, [r]ate or [t]ime? \n  > "
    err_msg = " is not a valid Distance problem.  "

    while tries < 3:
        prob_types['d'] = 'distance'
        prob_types['r'] = 'rate'
        prob_types['t'] = 'time'

        tries += 1

        sol = input(prompt)
        sol= sol.lower()
        if len(sol) > 0:
            for key in sol_types.keys():
                if key == sol or sol_types[key] == sol.lower:
                    return [key, sol_types[key]]
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

def get_time(solution_type):
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
        if len(myErr) > 0:
            print(myErr)
            input(prompt_cont)
            display.pop_screen(result_set)
           
'''
    output_line[0] = distance
    output_line[1] = time
'''  
def solution_for_distance():
    sol_type = result_set[-1][2][0]
    result_set[-1][1] = get_time(sol_type)
    display.pop_screen(result_set)

    result_set[-1][0] = get_rate(sol_type) * result_set[-1][1]/60/60 
    display.pop_screen(result_set)       

def solution_for_rate():
    sol_type = result_set[-1][2][0]
    result_set[-1][0] = get_distance()
    display.pop_screen(result_set)
    
    result_set[-1][1] = get_time(sol_type)
    display.pop_screen(result_set)

def solution_for_time():
    sol_type = result_set[-1][2][0]
    result_set[-1][0] = get_distance()
    display.pop_screen(result_set)
    
    result_set[-1][1] = (result_set[-1][0] /get_rate(sol_type)) * 60 * 60
    display.pop_screen(result_set)

def main():
    # cd __Dev\Python\ThinkPy\Distance
    while True:
        intent = get_intent()
        print(intent); input(); quit()
        result_set.append(['?', '?', get_solution_type()]) ############## don't append until you know we're solving an equation
        sol = result_set[-1][2][0]
        display.pop_screen(result_set)
        if sol == 'q':
            quit()
        elif sol == "d":
            solution_for_distance()
        elif sol == "r":
            solution_for_rate()
        elif sol == "t":
            solution_for_time()

    display.pop_screen(result_set)
    input(prompt_info)

if __name__ == '__main__':
    if len(argv) == 2:
        if argv[1] == '-t':
            pass 
    else: main()

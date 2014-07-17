#!c:\python\python

"""
----------------------------------------
D:\__Dev\Python\ThinkPy\Distance\main.py
/d/__Dev/Python/ThinkPy/Distance
----------------------------------------

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
time = 0.0
result_set = [] #--> a list of output_lines containing distance, time, and the 
                #    solution type

def delete(row):
    pass

def edit():
    from editor import editRow
    if len(result_set) == 1:
        editRow(result_set[0])  
    else:
        while True:
            display.pop_screen(result_set)
            choice = input('Which leg? ')
            if choice == 'q': return
            if len(choice) > 0 and utilities.isInt(choice):
                    if utilities.between(int(choice), 1, len(result_set)): editRow(result_set[int(choice) - 1]); return
                    else: input('%s is not a valid choice.  Press [Enter] to continue (or [q] to quit)' % choice)
            else: input('You must choose a leg between %d through %d.  Press [Enter] to continue (or [q] to quit)' % (1, len(result_set)))

def exit():
    if len(result_set) == 0 or (len(result_set) == 1 and (result_set[-1][0] == '?' or result_set[-1][1] == '?')):
        pass
    else:
        row = result_set[-1]
        #print(result_set); input(); quit()
        if len(result_set) >= 1:
            if row[0] == '?' or row[1] == '?':
                row[2] = ['q', 'quit']
            else: result_set.append(['?', '?', ['q', 'quit']])
        display.pop_screen(result_set)
    quit()
# :-----> Problem Solving Methods <------------------------------------------------
def legend():
    '''
        output_lines
        ------------
        [0] = distance
        [1] = time in seconds
        [2] = [choiceID, choice] -or- [solution type ID, solution type]

        choices
        -------
        [s]olve 
        [e]dit
        [d]elete
        [q]uit

        solution types
        --------------
        [d]istance
        [r]ate
        [t]ime

        NOTE: 
        output_lines with solution results accumulate in the
        results_set list 

    '''
    pass
  
def get_intent():
    if len(result_set) > 0:
        intents = {'s': '[s]olve', 'e': '[e]dit', 'd': '[d]elete', 'q': '[q]uit'}
    else:
        intents = {'s': '[s]olve', 'q': '[q]uit'}

    while True:

        if len(result_set) > 0:
            display.pop_screen('solving', result_set)
            print('What do you wanna do now?')
            for key in intents.keys():
                print('\t\t%s' % (intents[key]))
        else:
            display.pop_screen('initializing')

        response = input('Which action do you choose? ')
        resp = response.lower()
        if resp in intents.keys() or resp in intents.values():
            return resp[0] 
        else:
            input("'%s' is not a valid intent.  Press [ENTER] to continue." % response)

def get_solution_type():

    err_msg = "%s is not a valid Distance problem.\nTry d, r, t, or q to quit.\n" + prompt_cont
    solution_types = {'d': ('[d]istance', 'distance'), 'r': ('[r]ate', 'rate'), 't': ('[t]ime', 'time'),'q': ('[q]uit', 'quit')}
    
    while True:
        sol = input("Are you looking for [d]istance, [r]ate or [t]ime? \n  > ").lower()
        if len(sol) > 0 and (sol in solution_types.keys() or sol in solution_types.values()):
            return [sol[0], solution_types[sol[0]]]
        else:
            input(err_msg % sol)

    return 0

def solution_for_distance():
    sol_type = result_set[-1][2][0]
    result_set[-1][1] = get_time(sol_type)
    display.pop_screen('solving', result_set)

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

def get_distance():
    while True:
        distance = input(prompt_info + prompt_distance)
        if len(distance) > 0:
            if distance.lower() == 'q':
                exit()
            elif utilities.isNumeric(distance):
                return float(distance)
        else:
            print("%s is not a valid distance.  Press any key to continue." % distance)
    
def get_rate(solution_type):
    got_rate = 0

    while not got_rate:
        rate = input(prompt_info + prompt_rate)
        if len(rate) > 0:
            if rate.lower() == 'q': exit()
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

def get_time(solution_type):
    while True:
        time_string = input(prompt_info + prompt_time)
        if len(time_string) > 0:
            if time_string.lower() == 'q': exit()
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

#---------------------------------------------------------------------------------
           
#-----> Tests < ------------------------------------------------------------------

def test_delete():
    pass

def test_edit():
    tests_pop_data()
    main()
    
def tests_pop_data():
    global result_set
    result_set = [[56.25, 4500.0, ['d', ('[d]istance','distance')]]]
    result_set.append([50.0, 3900.0, ['r', ('[r]ate', 'rate')]])
    result_set.append([55.0, 6187.5, ['t', ('[t]ime', 'time')]])
    result_set.append([52.61416666666666, 3323.0, ['d', ('[d]istance','distance')]])
    display.pop_screen(result_set)
#---------------------------------------------------------------------------------

def main():
    # cd __Dev\Python\ThinkPy\Distance
    while True:
        choice = get_intent()
        #print(choice); input(); quit
        if choice == 's':
            result_set.append(['?', '?', get_solution_type()])
            sol = result_set[-1][2][0]
            display.pop_screen(result_set)
            if sol == "d":
                solution_for_distance()
            elif sol == "r":
                solution_for_rate()
            elif sol == "t":
                solution_for_time()
        else:
            if choice == 'q':
                exit()
            else:
                if choice == 'e':
                    edit()
                else: pass       ############## 

    display.pop_screen(result_set)
    input(prompt_info)

if __name__ == '__main__':
    if len(argv) == 2:
        if argv[1] == '--edit':
            test_edit()
        elif argv[1] == '--delete':
            test_delete()
        else: 
            output = '%s is not an option.\n'
            output += 'Try: %s %s'
            vars = (argv[1], '--edit', '--delete')
            print(output % vars)
    else: main()

import utilities

line_blank = "         :" + ' '*65 + ":"
line_dashed = "         :" + '-'*65 + ":"
line_test_head = "         1         2         3         4         5         6         7         8"
line_test_body = "12345678901234567890123456789012345678901234567890123456789012345678901234567890"

lm_titles = '         :' + (' ' * 16) + '<<< '
rm_titles = ' >>>' + (' ' * 19) + ':'

titles = {}
titles['d'] = lm_titles + "Distance = Rate X Time" + rm_titles
titles['r'] = lm_titles + "Rate = Distance / Time" + rm_titles
titles['t'] = lm_titles + "Time = Distance / Rate" + rm_titles
titles['q'] = lm_titles + " Solution is complete " + rm_titles

lm_cols = '     :'
rm_cols = '     :'

pad_cols = ' ' * 8

title_cols =   "         :     Leg             Distance            Rate           Time     :"
title_totals = "         :     Legs            Distance            Rate           Time     :"
title_seps =   "         :     ----            --------            ----           ----     :"

lm_data = '         :'
rm_data = rm_cols # 14 spaces and the ':' 

def exit(distance, total_time, legs):
    #print(distance, total_time, legs); input()
    if legs != 0:
        print(line_blank + '\n' + line_dashed + '\n' + line_blank)
        print(title_totals + '\n' + title_seps + '\n' + line_blank)
        output_line = lm_data + (' ' * 7 + str(legs))
        dist = utilities.format_number(str(distance), 2, 1)
        output_line += (' ' * (21 - len(dist))) + str(dist)
        hours = total_time / 60 / 60
        #print(distance, total_time, hours, distance/total_time); input()
        rate = utilities.format_number(str(distance / hours), 2, 1) # 41 - 44
        output_line += (' ' * (16 - len(rate))) + rate
        this_time = utilities.format_number(str(hours), 2, 1)
        output_line += (' ' * (15 - len(this_time))) + this_time + rm_data        
        print(output_line)
        print(line_blank + '\n' + line_dashed)
    else: utilities.clearScreen()
    quit()

def pop_screen(context, value = []):
    if context == 'editing':
        pop_screen_edit(value)
    elif context == 'initializing':
        pop_screen_init()
    elif context == 'solving':
        pop_screen_results(value)

def pop_screen_init():
    myFile = open('sample_screens\\display_initialize.txt', 'r')
    utilities.clearScreen()
    for line in myFile:
        print(line[:-1])
        
def pop_screen_results(result_set):
    utilities.clearScreen()
    print()
    print(line_dashed)
#    print(line_test_head) 
#    print(line_test_body)
    print(line_blank)
    print(titles[result_set[-1][2][0]])
    print(line_blank)
    print(line_dashed)
    print(line_blank)
    print(title_cols)
    print(title_seps)

    distance = 0.0
    total_time = 0.0 # in seconds
    counter = 0
    # ==> Populate the matrix with the calculated info

    for i in result_set: # [distance, seconds, [sol_type, ([s]ol, Sol)]]
        counter += 1
        legDist = i[0]
        legTime = i[1]
        legType = i[2][0]
        
        if legType == 'q':
           exit(distance, total_time, counter - 1)
        
        output_line = lm_data + (' ' * 7 + str(counter))[-8:]

        if legDist != '?':
            distance += legDist
            dist = utilities.format_number(legDist, 2, 1)
        else: dist='?'

        output_line += (' ' * (21 - len(dist))) + dist 

        if dist != '?' and legTime != '?':
#            print("In popScreen: i[0] =",i[0],"i[1] =",i[1])
#            input()
            hours = legTime / 60 / 60
            rate = utilities.format_number(legDist / hours, 2, 1) # 41 - 44
        else: rate = '?'

        output_line += (' ' * (16 - len(rate))) + rate

        if legTime != '?':  # 61 - 63
            this_time = utilities.format_number(legTime/60/60, 2, 1)
            total_time += legTime 
        else: this_time = '?'

        output_line += (' ' * (15 - len(this_time))) + this_time + rm_data ####################
        
        print(output_line)

    for i in range(42-len(result_set)): # <-- fix this to show the totals
        print(line_blank)
    print(line_dashed, '\n')

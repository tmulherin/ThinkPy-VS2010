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

title_cols =   "         :     Leg             Distance          Rate             Time     :"
title_totals = "         :     Sum             Distance          Rate             Time     :"
title_seps =   "         :     ---             --------          ----             ----     :"

lm_data = '         :'
rm_data = rm_cols # 14 spaces and the ':' 


def pop_screen(result_set):
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
    for i in result_set: # result_set is a list of lists...
        counter += 1
        solution_type = i[2][0]
        if solution_type == 'q':
            quit(result_set, distance, total_time, counter -1)
            return 0
        
        output_line = lm_data + (' ' * 7 + str(counter))[-8:]

        if i[0] != '?':
            dist = utilities.format_number(i[0], 2, 1)
            distance += i[0]
        else: dist='?'
        output_line += (' ' * (21 - len(dist))) + dist 

        if i[0] != '?' and i[1] != '?':
#            print("In popScreen: i[0] =",i[0],"i[1] =",i[1])
#            input()
            hours = i[1] / 60 / 60
            rate = utilities.format_number(i[0] / hours, 2, 1) # 41 - 44
        else: rate = '?'
        output_line += (' ' * (14 - len(rate))) + rate

        if i[1] != '?':  # 61 - 63
            this_time = utilities.format_number(i[1]/60/60, 2, 1)
            total_time += i[1] 
        else: this_time = '?'
        output_line += (' ' * (17 - len(this_time))) + this_time + rm_data
        
        print(output_line)

    for i in range(40-len(result_set)): # <-- fix this to show the totals
        print(line_blank)
    print(line_dashed, '\n')

def quit(result_set, distance, total_time, legs):
#    print(result_set); input()
    print(line_blank + '\n' + line_dashed + '\n' + line_blank)
    print(title_totals + '\n' + title_seps + '\n' + line_blank)
    output_line = lm_data + (' ' * 7 + str(legs))
    dist = utilities.format_number(str(distance), 2, 1)
    output_line += (' ' * (21 - len(dist))) + str(dist)
    hours = total_time / 60 / 60
    rate = utilities.format_number(str(distance / hours), 2, 1) # 41 - 44
    output_line += (' ' * (14 - len(rate))) + rate
    this_time = utilities.format_number(str(hours), 2, 1)
    output_line += (' ' * (17 - len(this_time))) + this_time + rm_data        
    print(output_line)
    print(line_blank + '\n' + line_dashed)

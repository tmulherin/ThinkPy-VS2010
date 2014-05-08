
import os
import utilities

line_blank = "   :" + ' '*78 + ":"
line_dashed = "   :" + '-'*78 + ":"
line_test_head = "         1         2         3         4         5         6         7         8"
line_test_body = "12345678901234567890123456789012345678901234567890123456789012345678901234567890"

lm_titles = '   :' + (' ' * 24) + '<<< '
rm_titles = ' >>>' + (' ' * 24) + ':'

titles = {}
titles['d'] = lm_titles + "Distance = Rate X Time" + rm_titles
titles['r'] = lm_titles + "Rate = Distance / Time" + rm_titles
titles['t'] = lm_titles + "Time = Distance / Rate" + rm_titles

lm_cols = '   :' + (" " * 16)
pad_cols = " " * 16
rm_cols = (" " * 14) + ":"

title_cols = lm_cols + "Distance" + pad_cols + "Rate" + pad_cols + "Time" + rm_cols
title_seps = lm_cols + "--------" + pad_cols + "----" + pad_cols + "----" + rm_cols

lm_data = '   :'
rm_data = rm_cols # 14 spaces and the ':' 

def clear_screen():
    os.system("cls")

def pop_screen(solution_type, result_set):
    clear_screen()
    print()
    print(line_dashed)
    print(line_blank)
    print(titles[solution_type])
    print(line_blank)
    print(line_dashed)
    print(line_blank)
    print(title_cols)
    print(title_seps)

    # ==> Populate the matrix with the calculated info
    for i in result_set: # result_set is a list of lists...

        dist = str(i[0]) # 17 - 24
        output_line = lm_data + (' ' * (24 - len(dist))) + dist 

        rate = str(i[1]) # 41 - 44
        output_line += (' ' * (20 - len(rate))) + rate

        tme =  str(i[2]) # 61 - 63
        output_line += (' ' * (20 - len(tme))) + tme + rm_data
        print(output_line)

#        print(lm_data + line_test_head + '\n' + lm_data + line_test_body)

    for i in range(29-len(result_set)): # <-- fix this to show the totals
        print(line_blank)

    print(line_dashed)
    print()
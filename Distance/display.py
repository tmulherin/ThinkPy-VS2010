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


def pop_screen(solution_type, result_set):
    utilities.clearScreen()
    print()
    print(line_dashed)
    print(line_blank)
    print(titles[solution_type])
    print(line_blank)
    print(line_dashed)
    print(line_blank)
    print(title_cols)
    print(title_seps)

    distance = 0.0
    time = 0.0
    # ==> Populate the matrix with the calculated info
    for i in result_set: # result_set is a list of lists...

        if i[0] != '?':
            dist = utilities.format_number(i[0], 2, 1)
            distance += i[0]
        else: dist='?'
        output_line = lm_data + (' ' * (24 - len(dist))) + dist 

        if i[0] != '?' and i[1] != '?':
            hours = i[1] / 60 / 60
            rate = utilities.format_number(i[0] / hours, 2, 1) # 41 - 44
        else: rate = '?'
        output_line += (' ' * (20 - len(rate))) + rate

        if i[1] != '?':  # 61 - 63
            tme = utilities.format_number(i[1]/60/60, 2, 1)
            time += i[1] 
        else: tme = '?'
        output_line += (' ' * (20 - len(tme))) + tme + rm_data
        
        print(output_line)

    for i in range(29-len(result_set)): # <-- fix this to show the totals
        print(line_blank)

    print(line_dashed)
    print()
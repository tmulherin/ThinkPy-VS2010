#!c:\python\python.exe
import display as disp, utilities as util 

def editRow(row):
    pass

def getRowToEdit(result_set):
    pass

def testEdit():
    result_set = [[56.25, 4500.0, ['d', 'distance']]]
    result_set.append([50.0, 3900.0, ['r', 'rate']])
    result_set.append([55.0, 6187.5, ['t', 'time']])
    result_set.append([52.61416666666666, 3323.0, ['d', 'distance']])
    result_set.append(['?', '?', ['q', 'quit']])
    disp.pop_screen(result_set)
    getRowToEdit(result_set)
if __name__ == '__main__':



    row = input("Please choose the leg to edit: ")
    if util.isInt(row):
        #==> result_set's last list item is '?', '?', 'q', 'quit'
        print(result_set[int(row) - 1])
    else:
        print(row, "is not a valid row")

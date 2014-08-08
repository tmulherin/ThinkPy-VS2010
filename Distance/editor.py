#!c:\python\python.exe
import display as disp, utilities as util, start 
from utilities import format_time_string 

def editRow(row):
    gotChoice = False
    while not gotChoice:
        util.clearScreen()
        #print(row); input(); quit()
        print('1) Solution Type: %s' % row[2][1][1])
        print('2) Distance:      %s' % row[0])
        interval = format_time_string(row[1])
        if interval[0] == 'interval':
            print('3) Time:          %s' % interval[1])
        else: pass   #-> there should be no error from this function
                     #   call - the time is guaranteed to be a float. 
        choice = input('Which line do you wish to edit? ')
        if choice == 'q':
            gotChoice = True
        elif util.isInt(choice) and util.between(int(choice), 1, 3):
                gotChoice = True
        else: input('%s is not a valid choice: press [ENTER] to continue' % choice)

    if choice == 'q': return

    if choice == '3':
        row[1] = start.get_time()
        editRow(row)
    elif choice == '2':
        row[0] = start.get_distance()
        editRow(row)
    elif choice == '1':
        input('rutwro')

def deleteRow(rowNumber):
    pass
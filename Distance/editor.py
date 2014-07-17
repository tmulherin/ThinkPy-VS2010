#!c:\python\python.exe
import display as disp, utilities as util 
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
        input('Fix Time')
    elif choice == '2':
        input('Fix Distance')
    elif choice == '1':
        input('rutwro')



def getRowToEdit(result_set):
    pass

def testEdit():

    getRowToEdit(result_set)
if __name__ == '__main__':



    row = input("Please choose the leg to edit: ")
    if util.isInt(row):
        #==> result_set's last list item is '?', '?', 'q', 'quit'
        print(result_set[int(row) - 1])
    else:
        print(row, "is not a valid row")

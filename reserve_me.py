desks = [(f'd{i}', {}) for i in range(1, 20)]
list_of_employees = []
list_of_id = []

def menu():
    
    print('----'.ljust(7) + 'MAIN MENU' + '----'.rjust(7))
    print('1.  Book a desk')
    print('2.  Cancel a reservation')
    print('3.  Show employees and reservations')
    print('4.  Add employee')
    print('5.  Remove employee from system')
    print('6.  EXIT')
    print(' ')

"""def show_reservations():
    
    from tabulate import tabulate
    
    headers = ['First Name', 'Last Name', 'Reservation code', 'Date', 'Desk number']    


    table1 = []
    table2 = []
    
    for f in list_of_employees:
        
        x = []
        x.append(f[0][0].split(' ')[0])
        x.append(f[0][0].split(' ')[1])
        
        table1.append(x)
    
    for d in desks:
        
        if len(d[1]) > 0:
            
            for a, b in d[1].items():
                    
                y = []    
                y.append(a)
                y.append(b)
                y.append(d[0])


            table2.append(y)
    
    print(tabulate(zip(table1, table2), headers=headers))
"""
#NEED SQL 

def show_employees():
    
    from tabulate import tabulate
    
    headers = ['First Name', 'Last Name', 'ID', 'Reservation codes']    


    table = []
    
    for f in list_of_employees:
        
        x = []
        x.append(f[0][0].split(' ')[0])
        x.append(f[0][0].split(' ')[1])
        x.append(f[0][1])
        x.append(f[1:])
        table.append(x)
    
    print(tabulate(table, headers=headers))

def add_employee():
    
    Input1 = input('First Name: ')
    
    Input2 = input('Last Name: ')
    
    name = Input1 + ' ' + Input2
        
    if len(list_of_employees) == 0:

        e = 1001

    else:

        e = list_of_employees[-1][0][1] + 1
    
    new_employee = [(name, e), ]
    
    list_of_employees.append(new_employee)


def remove_employee():
    
    Input1 = input("Employee's ID: ")
    
    for x in list_of_employees:
        
        if Input1 in x[0][1]:
            
            r = x
    
    list_of_employees.remove(r)

def gen_reservation_id():
    
    if list_of_id == []:
        
        g = 101
        
        list_of_id.append(g)
        
        return g
    
    else:
        
        g = list_of_id[-1] + 1
        
        list_of_id.append(g)
        
        return g

def book_desk():
    
    import random
    
    Input1 = input('Desk number or ENTER for any desk: ')
    #Check for correct input
    
    Input2 = input('Date (DD.MM): ')
    #Check for correct fomrat
    
    Input3 = input('First Name: ')
    
    Input4 = input('Last Name: ') #Check if employee on the list of employees. Ask if you want to add new employee
    
    name = Input3 + ' ' + Input4
    
    if Input1.isdigit():
        
        a = f'd{int(Input1)}'
        
        if Input2 not in desks[int(Input1) - 1][1].values():
            
            g = gen_reservation_id()
            
            desks[int(Input1) - 1][1][g] = Input2
            
            print(f'The desk number {int(Input1)} has beed booked on {Input2}')
            print(f'Your reservation ID is {g}')
        
        else:
            
            print('Sorry, this desk is already booked at this date. Please select another desk or date')
            
            book_desk()
            
    
    else:
        
        while True:
            
            a = random.choice(desks)[0]

            for x, y in enumerate(desks):

                if y[0] == a and (Input2 not in y[1].values()):

                    g = gen_reservation_id()

                    desks[x][1][g] = Input2

                    print(f'The desk number {x+1} has beed booked on {Input2}')
                    print(f'Your reservation ID is {g}')

                    break
                    
                    
                else:
                    
                    continue
            
                    #ADD EXCEPTION IF ALL DESKS ARE BOOKED IN THIS DATE
            break

    for x, y in enumerate(list_of_employees):
        
        if name in y[0]:
            
            list_of_employees[x].extend([g])
                
def del_reservation():
    
    Input1 = input('Desk number or Reservation Number: ')
     # ADD CHECK INPUT FOR APROPRIATE DATA
    
    if len(Input1) == 2 or len(Input1) == 1:
        
        #if dict is not empty:
        #else This desk has no reservation
        #EXIT
        
        dr = desks[int(Input1) - 1][1] #Delete Reservation
        
        print('Current reservations for this desk: ')
        print(list[dr.values()])
        #show_reservations(desks[int(Input1) - 1])
        #NEW FUNCTION FOR SHOWING RESERVATIONS
        #TO BE DONE
    
        if dr == {}:

            print('This desk has no reservations yet')
        
        else:
                
            reservation = True
            
            while reservation:

                Input2 = input('Write date of reservation you wish to cancel: ')
                # ADD CHECK INPUT FOR APROPRIATE DATA

                for x, y in dr.items():

                    if y == Input2:

                        to_del = x

                        reservation = False

                        break

                    else:

                        print('There is no such reservation')

                        continue
                        
            dr.pop(x)
            
            list_of_id.remove(x)

            print('Your reservation has been cancelled')
            
            
    elif len(Input1) == 3:
        
        for x, y in enumerate(desks):
            
            for c in y[1].keys():
                
                if c == int(Input1):
                    
                    delete = desks[x][1]         
                

        try:

            delete.pop(int(Input1))

            list_of_id.remove(int(Input1))

        except:

            print('There is no such ID reservation')

        else:

            print('Cancelation succesful')
            
            
            
    for a, b in enumerate(list_of_employees):

        if Input1 in b[1]:

            d = list_of_employees[x][1]
        
    try:

        d.remove(Input1)
        

    except:

        print('Ups, something went wrong. Please try again.')

    else:

        print('Your reservation has been cancelled')

            
            
                    
def reserve_me():
    
    reserve = True
    
    while reserve:
        
        menu()
        
        Input1 = input('\n: ') #check if digit
        
        #ADD CLEAR OUTPUT
        
        if Input1 == '1':
            
            booking = True
            
            while booking:
            
                book_desk()
                
                InputB = input('Would you like to make another reservation? y/n: ')
                
                if InputB.lower() == 'y':
                    
                    continue
                
                else:
                    
                    booking = False
                    

        elif Input1 == '2':
            
            deleting = True
            
            while deleting:
            
                del_reservation()
                
                InputD = input('Would you like to cancel another reservation? y/n: ')
                
                if InputD.lower() == 'y':
                    
                    continue
                
                else:
                    
                    deleting = False
                    
        
        elif Input1 == '3':
            
            show_employees()
                
            InputS = input('Press ENTER to continue: ')

            continue
            
        elif Input1 == '4':
            
            adding = True
            
            while adding:
                
                add_employee()
                
                InputA = input('Would you like to add next employee? y/n: ')
                
                if InputA.lower() == 'y':
                    
                    continue
                
                else:
                    
                    adding = False
        
        elif Input1 == '5':
            
            removing= True
            
            while removing:
                
                remove_employee()
                
                InputR = input('Would you like to remove next employee? y/n: ')
                
                if InputA.lower() == 'y':
                    
                    continue
                
                else:
                    
                    removing = False
            
            
        elif Input1 == '6':
            
            break
        
if __name__ == '__main__':
    
    reserve_me()
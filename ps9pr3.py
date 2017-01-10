# Devin Cheong
# devin@bu.edu
#
# ps9pr3.py - Date clients
#
#


from ps9pr2 import Date



def get_age_on(birthday, other):
    """ accepts two Date objects as parameters: one to represent a
    person’s birthday, and one to represent an arbitrary date. The function
    should then return the person’s age on that date as an integer.
    """
    x = birthday.copy()
    y = other.copy()
    yr = y.year - x.year
    if y.month < x.month:
        yr -= 1
    elif y.month == x.month:
        if y.day < x.day:
            yr -= 1
    return yr



def print_birthdays(filename):
    """accepts a string filename as a parameter. The function should then
    open the file that corresponds to that filename, read through the file,
    and print some information derived from that file.
    """
    file = open(filename, 'r')
    
    for line in file:
        
        fields = line.split(',')
        d = Date(int(fields[1]), int(fields[2]), int(fields[3]))

        


        print(fields[0] + ' (' + str(d) + ') (' + d.day_of_week() + ')')


    file.close()

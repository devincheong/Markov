# Devin Cheong
# devin@bu.edu
#
# ps9pr1.txt - Using string methods
#


def count_ignore_case(s, sub):
    """counts sub in s 
    """
    lowers = s.lower()
    lowersub = sub.lower()
    return lowers.count(lowersub)


    
    
    
def middle_name(fullname):
    """returns middle name
    """
    split = fullname.split()
    if len(split) >= 3:
        return split[1]
    else:
        return ''

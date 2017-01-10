# Devin Cheong
# devin#@bu.edu
#
# ps9pr2.py (Problem Set 9, Problem 2)
#
# A class to represent calendar dates
#

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, new_month, new_day, new_year):
        """ The constructor for objects of type Date. """
        self.month = new_month
        self.day = new_day
        self.year = new_year

    # The function for the Date class that returns a Date
    # object in a string representation.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this _can_ be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year. Otherwise, returns False.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date

#### Put your code for problem 2 below. ####

    def tomorrow(self):
        """changes the called object so that it
           represts one calendar day after the date that it originally represented.
        """
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year() == True:
            days_in_month[2] = 29

        self.day += 1

        if self.day > days_in_month[self.month]:
            self.day = 1
            self.month += 1
            if self.month > 12:
                self.month = 1
                self.year += 1
   

    def add_n_days(self, n):
        """ changes the calling object so that it represents n calendar days
        after the date it originally represented. Additionally, the method should
        print all of the dates from the starting date to the finishing date,
        inclusive of both endpoints.
        """
        if n == 0:
            print(self)
        else:
            print(self)
            for x in range(n):
                self.tomorrow()
                print(self)
                
                
                

    def __eq__(self, other):
        """returns True if the called object (self) and the argument (other)
        represent the same calendar date (i.e., if the have the same values for their
        day, month, and year attributes). Otherwise, this method should return False.
        """
        if self.day == other.day and self.month == other.month and self.year == other.year:
            return True
        else:
            return False


    def is_before(self, other):
        """returns True if the called object represents a calendar date that occurs
        before the calendar date that is represented by other. If self and other
        represent the same day, or if self occurs after other, the method should
        return False.
        """
        if self.year < other.year:
            return True
        elif self.month < other.month and self.year == other.year:
            return True
        elif self.day < other.day and self.month == other.month and self.year == other.year:
            return True
        else:
            return False


    def is_after(self, other):
        """returns True if the called object represents a calendar date that occurs
        after the calendar date that is represented by other. If self and other
        represent the same day, or if self occurs before other, the method should
        return False.
        """
        if self.year > other.year:
            return True
        elif self.month > other.month and self.year == other.year:
            return True
        elif self.day > other.day and self.month == other.month and self.year == other.year:
            return True
        else:
            return False

    def diff(self, other):
        """returns an integer that represents the number of days between self and other.
        """
        self1 = self.copy()
        other1 = other.copy()
        x = 0
        
        if self1.is_before(other1):
            while self1.is_before(other1):
                self1.tomorrow()
                x -= 1

        elif self1.is_after(other1):
            while self1.is_after(other1):
                other1.tomorrow()
                x += 1
    
        return x


    def day_of_week(self):
        """returns the day of the week in the form of a string 
        """
        day_of_week_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        d = Date(11, 14, 2016)   # Monday, index 0
        x = self.diff(d)
        c = x % 7
        return day_of_week_names[c]
              
       
    
        
        
    
            
        
        
        
        


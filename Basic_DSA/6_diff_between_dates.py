'''

    @Author: Shivraj Yelave
    @Date: 25-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Calculate Days Between Two Dates

'''

from datetime import datetime

def calculate_days_between_dates(date1, date2):
    '''
    Description:
        This function calculates the number of days between two dates.

    Parameters:
        date1 : tuple : a tuple representing the first date (year, month, day).
        date2 : tuple : a tuple representing the second date (year, month, day).

    Returns:
        int : the number of days between the two dates.
    '''
    # Convert tuples to datetime objects
    d1 = datetime(date1[0], date1[1], date1[2])
    d2 = datetime(date2[0], date2[1], date2[2])
    
    # Calculate the difference between dates
    delta = d2 - d1
    
    # Return the number of days as an integer
    return abs(delta.days)

def main():

    date1 = (2014, 6, 2)
    date2 = (2014, 7, 11)
    
    # Calculate and print the number of days between the dates
    days_between = calculate_days_between_dates(date1, date2)
    print(f"Difference between given dates is {days_between} days")

if __name__ == '__main__':
    # Call the main function when the script is executed
    main()

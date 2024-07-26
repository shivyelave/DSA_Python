'''

    @Author: Shivraj Yelave
    @Date: 25-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: User name

'''
import calendar

def print_calendar(month, year):
    '''
    Description:
        This function returns the calendar of a specific month and year as a string.

    Parameters:
        month : the month for which to display the calendar (1-12).
        year : the year for which to display the calendar.

    Returns:
        str : formatted calendar for the specified month and year.
    '''
    # Return the calendar for the given month and year as a multi-line string
    return calendar.month(year, month)

def main():
    # Print the calendar for December 2024
    try:
        # Ask the user to enter a month number
        month = int(input("Enter month in number (e.g., 7 for July): "))
        year = input("Enter year (e.g., 2024): ")

        
        # Check if the month is within the valid range
        if month < 1 or month > 12:
            raise ValueError("Month must be between 1 and 12.")
        if len(year)!=4:
            raise ValueError("Year Should be valid 4 digit number.")
        
        year=int(year)
        print(print_calendar(month,year))
        
    except ValueError as ve:
        # Handle specific ValueError exceptions (e.g., invalid integer or out of range)
        print(f"ValueError: {ve}")




if __name__ == '__main__':
    # Call the main function when the script is executed
    main()

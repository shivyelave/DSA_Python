'''

    @Author: Shivraj Yelave
    @Date: 27-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Append 'ing' or 'ly' to a String

'''

def add_ing_ly_at_end(string):
    """
    Description:
    Function to append 'ing' to a string unless it already ends in 'ing'. In that case, it appends 'ly'.

    Parameters:
    string (str): The input string to modify.

    Returns:
    str: The modified string with the appropriate suffix added.
    """
    # Check if the last three characters of the string are 'ing'
    if string[-3:] == 'ing':
        # If true, append 'ly' to the end of the string
        string += 'ly'
    else: 
        # If false, append 'ing' to the end of the string
        string += 'ing'
    # Return the modified string
    return string

def main():
    string = 'Rinning'  # Sample input string
    # Call the add_ing_ly_at_end function with the sample string and print the result
    print(add_ing_ly_at_end(string))

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

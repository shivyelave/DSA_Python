'''

    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Create a Set with Different Data Types

'''

def create_set():
    """
    Description:
    Function to create a set containing different data types: integer, string, float, and list.

    Returns:
    set: A set containing the provided integer, string, float, and list.
    """
    integer = int(input("Enter Integer: "))  # Prompt user to enter an integer
    string = str(input("Enter String: "))    # Prompt user to enter a string
    flt = float(input("Enter Float: "))      # Prompt user to enter a float
    # Prompt user to enter a list and split it by commas
    lst = input("Enter list (comma-separated values): ").split(',')

    # Convert list to a tuple to be able to add it to the set
    result_set = {integer, string, flt, tuple(lst)}  # Create a set with the provided values
    return result_set  # Return the created set

def main():
    # Call the create_set function and print the result
    print("Set:", create_set())

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

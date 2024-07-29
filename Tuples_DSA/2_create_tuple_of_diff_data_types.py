'''

    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Create a Tuple with Different Data Types

'''

def create_tuple_with_diff_datatypes():
    """
    Description:
    Function to create a tuple containing different data types: integer, string, float, and list.

    Returns:
    tuple: A tuple containing the provided integer, string, float, and list.
    """
    integer = int(input("Enter Integer: "))  # Prompt user to enter an integer
    string = str(input("Enter String: "))    # Prompt user to enter a string
    flt = float(input("Enter Float: "))      # Prompt user to enter a float
    lst = input("Enter list (comma-separated values): ").split(',')  # Prompt user to enter a list and split it by commas

    result_tuple = (integer, string, flt, lst)  # Create a tuple with the provided values
    return result_tuple  # Return the created tuple

def main():
    # Call the create_tuple_with_diff_datatypes function and print the result
    print("Tuple:", create_tuple_with_diff_datatypes())

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

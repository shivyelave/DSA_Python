'''


    @Author: Shivraj Yelave
    @Date: 30-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Create Multiplication Table Dictionary


'''

def table_dictionary(number):

    """

    Description:
        Function to create a dictionary representing the multiplication table of a given number.

    Parameters:
        number (int): The number for which the multiplication table is to be created.

    Returns:
        dict: A dictionary where keys are integers from 1 to 10, and values are the product of the key and the given number.
    
    """
    
    dictionary = {}  # Initialize an empty dictionary
    # Iterate through numbers 1 to 10
    for i in range(1, 11):
        dictionary[i] = i * number  # Set the key as the current number and the value as the product of the key and the given number
    return dictionary  # Return the dictionary containing the multiplication table

def main():
    # Define a sample number for the multiplication table
    number = 7  # Specify the number to generate the table for
    # Call the function to create the multiplication table dictionary and print the result
    print(f"Table of {number} is {table_dictionary(number)}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

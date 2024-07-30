'''


    @Author: Shivraj Yelave
    @Date: 30-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Generate Square Dictionary


'''

def square_dictionary(number):

    """

    Description:
        Function to generate a dictionary where the keys are integers from 1 to a specified number,
        and the values are the squares of these integers.

    Parameters:
        number (int): The highest integer to include in the dictionary.

    Returns:
        dict: A dictionary where the keys are integers from 1 to `number`, and the values are their squares.

    """
    
    square_dict = {}  # Initialize an empty dictionary to store the results

    # Iterate through the range from 1 to the specified number (inclusive)
    for key in range(1, number + 1):
        # Assign the square of the key to the dictionary
        square_dict[key] = key * key

    return square_dict  # Return the generated dictionary

def main():
    # Define the number for which to generate the square dictionary
    number = 7

    # Call the function to generate the square dictionary and print the result
    print(square_dictionary(number))

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

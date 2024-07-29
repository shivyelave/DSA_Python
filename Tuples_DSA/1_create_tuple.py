'''


    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Create Tuple from List
    

'''

def create_tuple(numbers):
    """
    Description:
    Function to convert a list of numbers into a tuple.

    Parameters:
    numbers (list): The input list of numbers to convert.

    Returns:
    tuple: A tuple containing the elements of the input list.
    """
    numbers = tuple(numbers)  # Convert the list to a tuple
    return numbers

def main():
    numbers = [2, 3, 4, 5, 6, 7]  # Sample list of numbers
    # Call the create_tuple function and print the result
    print("Type:", type(create_tuple(numbers)))
    print("Tuple:", create_tuple(numbers))

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

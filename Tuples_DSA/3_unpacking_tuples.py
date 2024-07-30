'''

    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Unpack Tuples

'''

def unpacking_tuples(tuples):
    """
    Description:
    Function to unpack a tuple into three separate variables.

    Parameters:
    tuples (tuple): The input tuple containing three elements.

    Returns:
    tuple: The three unpacked elements from the input tuple.
    """
    (tuple1, tuple2, tuple3) = tuples  # Unpack the input tuple into three variables
    return tuple1, tuple2, tuple3  # Return the unpacked variables

def main():
    input_tuple = (1, 'saj', True)  # Sample input tuple
    # Unpack the tuple using the unpacking_tuples function
    tuple1, tuple2, tuple3 = unpacking_tuples(input_tuple)
    # Print the unpacked variables
    print("Unpacked tuples:", tuple1, tuple2, tuple3)

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

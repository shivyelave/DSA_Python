'''

    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Clone a Tuple

'''

def clone_tuple(input_tuple):
    """
    Description:
    Function to clone a tuple.

    Parameters:
    input_tuple (tuple): The input tuple to clone.

    Returns:
    tuple: A clone of the input tuple.
    """
    clone = input_tuple[:]  # Create a clone of the input tuple
    return clone  # Return the cloned tuple

def main():
    sample_tuple = (2, 3, 'sd', 21, 'wwqqw')  # Sample input tuple
    # Call the clone_tuple function and print the cloned tuple
    print("Cloned tuple:", clone_tuple(sample_tuple))

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

'''

    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Reverse Tuple

'''

def reverse_tuple(input_tuple):
    """
    Description:
    Function to reverse the elements of a given tuple.

    Parameters:
    input_tuple (tuple): The input tuple to reverse.

    Returns:
    tuple: The reversed tuple.
    """
    # Reverse the tuple using slicing
    return input_tuple[::-1]

def main():
    tuple = (2, 12, 23, 34, 2, 41, 24, 76)  # Sample input tuple

    print(f"Reversed tuple: {reverse_tuple(tuple)}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

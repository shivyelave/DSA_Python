'''

    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Check Element in Tuple

'''

def element_in_tuple(input_tuple, element):
    """
    Description:
    Function to check if an element is present in a tuple.

    Parameters:
    input_tuple (tuple): The input tuple to search within.
    element: The element to check for in the tuple.

    Returns:
    bool: True if the element is found in the tuple, False otherwise.
    """
    return element in input_tuple

def main():
    input_tuple = (2, 3, 54, 2, 4, 3, 5)  # Sample input tuple
    element = 534  # Element to check for in the tuple
    # Call the element_in_tuple function and print the result
    print(f"Is the element present: {element_in_tuple(input_tuple, element)}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

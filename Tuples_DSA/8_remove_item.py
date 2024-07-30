'''

    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Remove Item from Tuple

'''

def remove_item_from_tuple(input_tuple, element):
    """
    Description:
    Function to remove a specified element from a tuple.

    Parameters:
    input_tuple (tuple): The input tuple from which to remove the element.
    element (any): The element to remove from the tuple.

    Returns:
    tuple: The tuple after the specified element has been removed.
    """
    input_tuple = list(input_tuple)  # Convert tuple to list
    if element in input_tuple:
        input_tuple.remove(element)  # Remove the element if it exists
    return tuple(input_tuple)  # Convert list back to tuple

def main():
    tuple = (2, 12, 23, 34, 2, 41, 24, 76)  # Sample input tuple
    element_to_remove = 12  # Element to remove
    # Call the remove_item_from_tuple function and print the result
    print(f"Tuple after removing {element_to_remove} is {remove_item_from_tuple(tuple, element_to_remove)}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

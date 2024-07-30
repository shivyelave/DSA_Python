'''

    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Convert List to Tuple

'''

def list_to_tuple(input_list):
    """
    Description:
    Function to convert a list to a tuple.

    Parameters:
    input_list (list): The input list to convert to a tuple.

    Returns:
    tuple: The converted tuple.
    """
    return tuple(input_list)

def main():
    lst = [2, 3, 24, 1, 23, 'wqq', 'qeqw', 'wfsa']  # Sample input list
    print("Type:", type(list_to_tuple(lst) ))  # Print the type of the converted tuple
    print("Tuple:", list_to_tuple(lst) )  # Print the converted tuple

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

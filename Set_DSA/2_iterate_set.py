'''

    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Iterate Over a Set

'''

def iterate_set(input_set):
    """
    Description:
    Function to iterate over a set and print its elements.

    Parameters:
    input_set (set): The set to iterate over.

    Returns:
    None
    """
    for element in input_set:
        print(element, end=" ")  # Print each element of the set, separated by space

def main():
    input_set = {2, 3, 4, 5, 21, 34, 46}  # Sample input set
    iterate_set(input_set)  # Call the function to print elements of the set

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

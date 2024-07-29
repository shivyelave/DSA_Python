'''

    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Find Repeated Items in a Tuple

'''

def tuple_repeated_items(input_tuple):
    """
    Description:
    Function to find repeated items in a tuple.

    Parameters:
    input_tuple (tuple): The input tuple to check for repeated items.

    Returns:
    tuple: A tuple containing repeated items.
    """
    repeated = []  # Initialize an empty list to store repeated items
    for index in range(len(input_tuple)):
        # Check if the current item appears more than once in the tuple
        if input_tuple[index] in input_tuple[:index] + input_tuple[index+1:]:
            # If it's not already in the repeated list, add it
            if input_tuple[index] not in repeated:
                repeated.append(input_tuple[index])

    return tuple(repeated)  # Convert the list to a tuple and return

def main():
    input_tuple = (2, 3, 54, 2, 4, 3, 5)  # Sample input tuple
    # Call the tuple_repeated_items function and print the result
    print("Repeated items in the tuple:", tuple_repeated_items(input_tuple))

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

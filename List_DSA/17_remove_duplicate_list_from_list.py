'''


    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Remove Duplicate Lists from a List of Lists
    

'''

def remove_duplicate_list_from_list(list_of_list):
    """
    Description:
    Function to remove duplicate lists from a list of lists. It preserves the order of the first occurrence of each sublist.

    Parameters:
    list_of_list (list): The input list containing sublists.

    Returns:
    list: A list of sublists with duplicates removed.
    """
    unique = []  # Initialize an empty list to store unique sublists
    
    # Iterate through each sublist in the input list of lists
    for sublist in list_of_list:
        # Check if the current sublist is not already in the unique list
        if sublist not in unique:
            unique.append(sublist)  # Add the sublist to the unique list
    
    return unique  # Return the list with duplicates removed

def main():
    list_of_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]  # Sample list of lists
    # Call the remove_duplicate_list_from_list function and print the result
    print(remove_duplicate_list_from_list(list_of_list))

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

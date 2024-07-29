'''

    @Author: Shivraj Yelave
    @Date: 28-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Check for Common Elements in Two Lists

'''

def isCommon(list1, list2):
    """
    Description:
    Function to check if there are any common elements between two lists.

    Parameters:
    list1 (list): The first input list.
    list2 (list): The second input list.

    Returns:
    bool: True if there is at least one common element, False otherwise.
    """
    # Iterate through each member in the first list
    for member in list1:
        # Check if the current member is in the second list
        if member in list2:
            return True  # Return True if a common element is found
    
    return False  # Return False if no common elements are found

def main():
    list1 = [11, 12, 13, 14, 16, 1]  # Sample first list
    list2 = [21, 23, 22, 24, 25, 11]  # Sample second list
    # Call the isCommon function and print the result
    print("Is there a common element:", isCommon(list1, list2))

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

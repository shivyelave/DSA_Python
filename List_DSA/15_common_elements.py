'''

    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Find Common Elements in Two Lists
    

'''

def common_elements(list1, list2):
    """
    Description:
    Function to find common elements in two lists and remove duplicates from the result.

    Parameters:
    list1 (list): The first input list containing numbers.
    list2 (list): The second input list containing numbers.

    Returns:
    list: A list of common elements with duplicates removed.
    """
    # Find common elements between the two lists
    common_elements_list = [number for number in list1 if number in list2]
    
    # Remove duplicates by converting the list to a set and back to a list
    common_elements_list = list(set(common_elements_list))
    
    return common_elements_list  # Return the list with duplicates removed

def main():
    list1 = [2, 4, 1, 12, 1, 4, 22, 64, 1, 2, 22]  # Sample first list of numbers
    list2 = [92, 80, 23, 35, 64, 22, 1, 2, 22]  # Sample second list of numbers
    # Call the common_elements function and print the result
    print(f"Common elements list: {common_elements(list1, list2)}")


# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

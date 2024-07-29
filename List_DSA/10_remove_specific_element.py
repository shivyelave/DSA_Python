'''

    @Author: Shivraj Yelave
    @Date: 28-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Remove Specific Elements from a List

'''

def remove_specific_element(input_list):
    """
    Description:
    Function to remove specific elements from a list. It removes the first, fifth, and sixth elements.

    Parameters:
    input_list (list): The input list from which elements will be removed.

    Returns:
    list: The list after removing the specific elements.
    """
    # List of elements to remove (the first, fifth, and sixth elements)
    elements_to_remove = [input_list[0], input_list[4], input_list[5]]
    
    # Iterate through each element to remove and remove it from the input list
    for element in elements_to_remove:
        input_list.remove(element)
    
    return input_list  # Return the edited list

def main():
    input_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']  # Sample input list
    # Call the remove_specific_element function and print the result
    print("Edited list is:", remove_specific_element(input_list))

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

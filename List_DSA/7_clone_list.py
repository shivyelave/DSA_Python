'''

    @Author: Shivraj Yelave
    @Date: 28-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Clone a List

'''

def clone_list(input_list):
    """
    Description:
    Function to create a clone of the input list.

    Parameters:
    input_list (list): The input list to clone.

    Returns:
    list: A new list that is a clone of the input list.
    """
    new_list = []  # Initialize an empty list to store the cloned elements
    
    # Iterate through each element in the input list
    for element in input_list:
        new_list.append(element)  # Append the element to the new list
    
    return new_list  # Return the cloned list

def main():
    list = [2, 4, 1, 12, 1, 4, 22, 1, 2, 22]  # Sample list of numbers
    # Call the clone_list function and print the result
    print(f"Copied list: {clone_list(list)}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

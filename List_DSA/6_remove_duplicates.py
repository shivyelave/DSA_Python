'''

    @Author: Shivraj Yelave
    @Date: 28-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Remove Duplicates from a List

'''

def remove_duplicate(number_list):
    """
    Description:
    Function to remove duplicate numbers from a list.

    Parameters:
    number_list (list): The input list containing numbers.

    Returns:
    list: A list with duplicates removed, preserving the original order.
    """
    unique_list = []  # Initialize an empty list to store unique numbers
    
    # Iterate through each number in the input list
    for number in number_list:
        # If the number is not already in the unique list, append it
        if number not in unique_list:
            unique_list.append(number)

    return unique_list  # Return the list with duplicates removed

def main():
    list = [2, 4, 1, 12, 1, 4, 22, 1, 2, 22]  # Sample list of numbers
    # Call the remove_duplicate function and print the result
    print(f"Unique list: {remove_duplicate(list)}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

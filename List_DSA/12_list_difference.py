'''


    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Remove Duplicates from a List
    

'''

def list_difference(list1,list2):
    """
    Description:
    Function to remove duplicate numbers from a list.

    Parameters:
    number_list (list): The input list containing numbers.

    Returns:
    list: A list with duplicates removed, preserving the original order.
    """
    difference = []  # Initialize an empty list to store unique numbers
    
    # Iterate through each number in the input list
    for number in list1:
        # If the number is not already in the unique list, append it
        if number not in list2:
            difference.append(number)
    for number in list2:
        # If the number is not already in the unique list, append it
        if number not in list1:
            difference.append(number)
    difference=set(difference)
    return list(difference)  # Return the list with duplicates removed

def main():
    list1 = [2, 4, 1, 12, 1, 4, 22, 1, 2, 22]  # Sample list of numbers
    list2 = [92,80,23,35,64,22, 1, 2, 22]  # Sample list of numbers
    # Call the remove_duplicate function and print the result
    print(f"Difference list: {list_difference(list1,list2)}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

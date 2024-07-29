'''

    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Append Elements from One List to Another

'''

def append_lists(list1, list2):
    """
    Description:
    Function to append elements from the second list to the first list.

    Parameters:
    list1 (list): The first input list.
    list2 (list): The second input list to append to the first list.

    Returns:
    list: The first list after appending elements from the second list.
    """
    # Iterate through each number in the second list
    for number in list2:
        list1.append(number)  # Append the number to the first list

    return list1  # Return the modified first list

def main():
    list1 = [2, 4, 1, 12, 1, 4, 22, 1, 2, 22]  # Sample first list of numbers
    list2 = [92, 80, 23, 35, 64, 22, 1, 2, 22]  # Sample second list of numbers
    # Call the append_lists function and print the result
    print(f"Appended list: {append_lists(list1, list2)}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

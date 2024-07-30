'''
    @Author: Shivraj Yelave
    @Date: 30-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Count Occurrences in Array
'''

import array

def number_of_occurrence(arr, element):
    """
    Description:
        Function to count the number of occurrences of an element in the array.

    Parameters:
        arr (array.array): The array to search in.
        element (int): The element to count occurrences of.

    Returns:
        int: The number of times the element occurs in the array.
    """
    count = 0  # Initialize count to 0

    # Iterate through the array and count occurrences of the element
    for index in range(len(arr)):
        if arr[index] == element:
            count += 1

    return count  # Return the count

def main():
    # Create an array of integers
    arr = array.array('i', [1, 2, 3, 2, 5, 7, 8, 3, 24, 4, 2, 1, 4, 7, 2, 4, 46, 9, 2, 3, 2])
    element = 2  # Element to count in the array

    # Print the number of occurrences of the element in the array
    print(f"Number {element} occurs {number_of_occurrence(arr, element)} times in array {arr.tolist()}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

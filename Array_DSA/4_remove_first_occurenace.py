'''
    @Author: Shivraj Yelave
    @Date: 30-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Remove First Occurrence in Array
'''

import array

def remove_first_occurrence(arr, element):
    """
    Description:
        Function to remove the first occurrence of an element in the array.

    Parameters:
        arr (array.array): The array to search in.
        element (int): The element to remove.

    Returns:
        array.array: The array with the first occurrence of the element removed.
    """
    # Iterate through the array and remove the first occurrence of the element
    for index in range(len(arr)):
        if arr[index] == element:
            arr.remove(element)  # Remove the first occurrence of the element
            break

    return arr  # Return the modified array

def main():
    # Create an array of integers
    arr = array.array('i', [1, 2, 3, 2, 5, 7, 8, 3, 24, 4, 2, 1, 4, 7, 2, 4, 46, 9, 2, 3, 2])
    element = 2  # Element to remove from the array

    # Print the array after removing the first occurrence of the element
    print(f"Array after removing the first occurrence of {element}: {remove_first_occurrence(arr, element)}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

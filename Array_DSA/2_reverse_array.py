'''
    @Author: Shivraj Yelave
    @Date: 30-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Reverse Array Elements

'''

import array

def reverse_array(arr):
    """
    Description:
        Function to reverse the elements of the array in place.

    Parameters:
        arr (array.array): The array to reverse.

    Returns:
        array.array: The reversed array.
    """
    # Loop through half of the array and swap elements from both ends
    for index in range(len(arr) // 2):
        arr[index], arr[len(arr) - 1 - index] = arr[len(arr) - 1 - index], arr[index]
    return arr

def main():
    # Create an array of integers
    arr = array.array('i', [1, 2, 3, 4, 5])
    print(f"Original array: {arr}")
    
    # Reverse the array
    reversed_arr = reverse_array(arr)
    print(f"Reversed array: {reversed_arr}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

'''


    @Author: Shivraj Yelave
    @Date: 30-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Create and Print Array



'''

import array

def create_array():

    """

    Description:
        Function to create an array of integers by taking input from the user.

    Returns:
        array.array: An array of integers.

    """
    
    # Initialize an empty array of integers
    arr = array.array('i', [0]*5)  # Create an array of size 5 with integer type
    print("Enter 5 numbers one by one and press enter:")
    
    # Loop through each index of the array and take input from the user
    for index in range(5):
        arr[index] = int(input())
    
    return arr

def print_array(arr):
    """
    Description:
        Function to print the elements of the array.

    Parameters:
        arr (array.array): The array to print.
    """
    # Loop through each element in the array and print it
    for index in range(len(arr)):
        print(f'Array element at index {index}: {arr[index]}')

def main():
    # Create an array by calling create_array function
    arr = create_array()
    
    # Print the array elements by calling print_array function
    print_array(arr)

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()


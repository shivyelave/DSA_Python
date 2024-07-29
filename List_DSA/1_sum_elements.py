'''


    @Author: Shivraj Yelave
    @Date: 28-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Sum Elements of a List

    
'''

def sum_elements(numbers_list):
    """
    Description:
    Function to calculate the sum of all elements in a list of numbers.

    Parameters:
    numbers_list (list): The input list containing numbers to sum.

    Returns:
    int: The sum of all numbers in the list.
    """
    sum = 0  # Initialize the sum to 0
    
    # Iterate through each number in the list
    for number in numbers_list:
        sum += number  # Add the current number to the sum
    
    return sum  # Return the total sum

def main():
    list = [2, 4, 12, 43, 53, 66, 34, 23]  # Sample list of numbers
    # Call the sum_elements function and print the result
    print("Sum:", sum_elements(list))

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

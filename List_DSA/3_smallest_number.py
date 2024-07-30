'''

    @Author: Shivraj Yelave
    @Date: 28-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Find Smallest Number in a List

'''

def smallest_number(number_list):
    """
    Description:
    Function to find the smallest number in a list of numbers.

    Parameters:
    number_list (list): The input list containing numbers to evaluate.

    Returns:
    int: The smallest number in the list.
    """
    # Initialize the smallest variable to the first element of the list
    smallest = number_list[0]

    # Iterate through each number in the list
    for number in number_list:
        # If the current number is smaller than the smallest, update smallest
        if number < smallest:
            smallest = number

    return smallest  # Return the smallest number

def main():
    list = [2, 4, 12, 43, 53, 66, 34, 23]  # Sample list of numbers
    # Call the smallest_number function and print the result
    print(f"Smallest number in {list} is {smallest_number(list)}.")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

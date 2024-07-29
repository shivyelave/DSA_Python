'''

    @Author: Shivraj Yelave
    @Date: 28-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Product of Elements in a List

'''

def product_elements(numbers_list):
    """
    Description:
    Function to calculate the product of all elements in a list of numbers.

    Parameters:
    numbers_list (list): The input list containing numbers to multiply.

    Returns:
    int: The product of all numbers in the list.
    """
    product = 1  # Initialize the product to 1
    
    # Iterate through each number in the list
    for number in numbers_list:
        product *= number  # Multiply the current number to the product
    
    return product  # Return the total product

def main():
    list = [2, 4, 12, 43, 53]  # Sample list of numbers
    # Call the product_elements function and print the result
    print("Product:", product_elements(list))

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

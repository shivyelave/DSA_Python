'''

    @Author: Shivraj Yelave
    @Date: 27-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Reverse a String

'''

def reverse_string(string):
    """
    Description:
    Function to reverse a given string.

    Parameters:
    string (str): The input string to reverse.

    Returns:
    str: The reversed string.
    """
    # Return the reversed string using slicing
    return string[::-1]

def main():
    string = "Shiv yelave"  # Sample input string
    # Call the reverse_string function and print the result
    print(reverse_string(string))

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

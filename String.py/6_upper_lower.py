'''

    @Author: Shivraj Yelave
    @Date: 27-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Convert String to Uppercase and Lowercase

'''

def upper_lower(string):
    """
    Description:
    Function to convert a string to both uppercase and lowercase.

    Parameters:
    string (str): The input string to modify.

    Returns:
    tuple: A tuple containing the uppercase and lowercase versions of the input string.
    """
    # Convert the string to uppercase and lowercase, then return them as a tuple
    return string.upper(), string.lower()

def main():
    # Prompt the user to enter a string
    input_string = input("Enter string: ")
    
    # Call the upper_lower function with the input string and unpack the result
    upper, lower = upper_lower(input_string)
    
    # Print the uppercase version of the string
    print(f"Uppercase: {upper}")
    
    # Print the lowercase version of the string
    print(f"Lowercase: {lower}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

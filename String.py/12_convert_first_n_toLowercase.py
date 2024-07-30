'''

    @Author: Shivraj Yelave
    @Date: 27-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Convert First N Characters of a String to Lowercase

'''

def convert_lower(string, number):
    """
    Description:
    Function to convert the first 'number' characters of a string to lowercase.

    Parameters:
    string (str): The input string to modify.
    number (int): The number of characters to convert to lowercase.

    Returns:
    str: The modified string with the first 'number' characters in lowercase.
    """
    # Convert the first 'number' characters to lowercase
    output = string[:number].lower()
    
    # Return the modified string by concatenating the lowercase portion with the rest of the string
    return output + string[number:]

def main():
    string = 'SNDCLSNSAJBLCJBASB'  # Sample input string
    number = 3  # Number of characters to convert to lowercase
    # Call the convert_lower function and print the result
    print(convert_lower(string, number))

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

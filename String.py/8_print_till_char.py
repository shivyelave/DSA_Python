'''

    @Author: Shivraj Yelave
    @Date: 27-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Print String Until a Specific Character

'''

def print_string_till_char(string, char):
    """
    Description:
    Function to print characters of a string until a specific character is encountered.

    Parameters:
    string (str): The input string to process.
    char (str): The character at which to stop processing the string.

    Returns:
    str: The substring of the input string up to (but not including) the specified character.
    """
    output = ''  # Initialize an empty string to hold the result

    # Loop through each character in the input string
    for letter in string:
        # If the current character is not the specified stop character
        if letter != char:
            # Append the current character to the output string
            output += letter
        else:
            # If the stop character is encountered, exit the loop
            break
    
    # Return the resulting substring
    return output

def main():
    input_string = "https://www.w3resource.com/python-exercises-shivyelave"  # Sample input string
    break_char = '-'  # Character at which to stop processing the string
    # Call the print_string_till_char function with the input string and stop character, then print the result
    print(print_string_till_char(input_string, break_char))

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

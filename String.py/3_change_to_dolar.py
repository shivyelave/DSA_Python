'''

    @Author: Shivraj Yelave
    @Date: 26-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Replace Subsequent Occurrences of First Character with Dollar Sign

'''

def add_dollar(string):
    """
    Description:
    Function to replace all subsequent occurrences of the first character of each word with a dollar sign.

    Parameters:
    string (str): The input string with words to modify.

    Returns:
    str: The modified string with replacements.
    """
    string = string.split(' ')  # Split the string into words
    res_str = ''  # Initialize the resulting string

    for word in string:
        word = word[0] + word[1:].replace(word[0], '$')  # Replace subsequent occurrences of the first character with '$'
        res_str = res_str + word + ' '  # Append the modified word to the result string
    return res_str

def main():
    string = "hiih hllho hohw hah"  # Sample input string
    print(add_dollar(string))  # Call the add_dollar function and print the result

if __name__ == "__main__":
    main()  # Execute the main function if the script is run directly

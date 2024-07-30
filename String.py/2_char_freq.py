'''

    @Author: Shivraj Yelave
    @Date: 26-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Character Frequency in a String

'''

def char_freq(string):
    """
    Description:
    Function to count the frequency of each character in a given string after removing spaces.

    Parameters:
    string (str): The string in which to count the characters.

    Returns:
    dict: A dictionary with characters as keys and their frequencies as values.
    """
    string = string.replace(' ', '')  # Remove all spaces from the string
    dictionary = {}  # Initialize an empty dictionary to store character frequencies
    for char in string:
        if char in dictionary:
            dictionary[char] += 1  # Increment the count if the character is already in the dictionary
        else:
            dictionary[char] = 1  # Initialize the count if the character is not in the dictionary
    return dictionary

def main():
    string_input = input("Enter a string: ")  # Prompt the user to enter a string
    print(char_freq(string_input))  # Call the char_freq function and print the resulting frequency dictionary

if __name__ == '__main__':
    main()  # Execute the main function if the script is run directly

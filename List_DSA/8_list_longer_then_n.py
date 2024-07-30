'''

    @Author: Shivraj Yelave
    @Date: 28-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: List Longest Words Longer Than n Characters

'''

def list_longest_words_than_n(string_list, length):
    """
    Description:
    Function to list words from the input list that are longer than a specified length.

    Parameters:
    string_list (list): The input list containing strings.
    length (int): The length to compare against.

    Returns:
    list: A list of words from the input list that are longer than the specified length.
    """
    required_list = []  # Initialize an empty list to store the required words
    
    # Iterate through each string in the input list
    for string in string_list:
        # Check if the length of the string is greater than the specified length
        if len(string) > length:
            required_list.append(string)  # Append the string to the required list
    
    return required_list  # Return the list of required words

def main():
    string_list = ['shiv', 'yelave', 'b', 'a', 'b', 'an']  # Sample list of strings
    length = 2  # Specified length to compare against
    # Call the list_longest_words_than_n function and print the result
    print("Required list:", list_longest_words_than_n(string_list, length))

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

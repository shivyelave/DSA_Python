'''

    @Author: Shivraj Yelave
    @Date: 27-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Find the Length of the Longest String in a List

'''

def longest_string_length(string_list):
    """
    Description:
    Function to find the length of the longest string in a given list of strings.

    Parameters:
    string_list (list): The input list of strings to search.

    Returns:
    int: The length of the longest string in the list.
    """
    # Initialize largest_word_length with the length of the first string in the list
    largest_word_length = len(string_list[0])
    
    # Iterate through each word in the list
    for word in string_list:
        # If the current word's length is greater than largest_word_length
        if len(word) > largest_word_length:
            # Update largest_word_length to the current word's length
            largest_word_length = len(word)
    
    # Return the length of the longest string
    return largest_word_length

def main():
    word_list = ['hii','hello','hm','shivraj','nnn','aks']  # Sample list of strings
    # Call the longest_string_length function with the sample list and print the result
    print("Longest string length is", longest_string_length(word_list))

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

'''

    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Split List of Strings by First Character

'''

def split_by_first_char(string_list):
    """
    Description:
    Function to split a list of strings into sublists based on their first character.

    Parameters:
    string_list (list): The input list containing strings.

    Returns:
    list: A list of sublists, where each sublist contains strings starting with the same character.
    """
    list_group = []  # Initialize an empty list to store the grouped sublists
    
    # Iterate through the lowercase alphabet
    for alphabet in range(ord('a'), ord('z') + 1):
        same_start = []  # Initialize an empty list to store strings with the same starting character
        
        # Iterate through each word in the input string list
        for word in string_list:
            # Check if the current word starts with the current alphabet character
            if chr(alphabet) == word[0].lower():
                same_start.append(word)
        
        # If there are any words with the current starting character, add the sublist to the main list
        if len(same_start):
            list_group.append(same_start)
    
    return list_group  # Return the list of grouped sublists

def main():
    string_list = ['abs', 'bsaj', 'jshks', 'asnj', 'ssjba', 'abab', 'jasd']  # Sample list of strings
    # Call the split_by_first_char function and print the result
    print(split_by_first_char(string_list))

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

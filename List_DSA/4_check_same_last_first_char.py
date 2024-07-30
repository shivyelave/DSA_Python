'''

    @Author: Shivraj Yelave
    @Date: 28-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Count Strings with Same Start and End Character

'''

def check_number_of_string_with_same_char_at_start_end(string_list):
    """
    Description:
    Function to count the number of strings in a list that have the same character 
    at the start and end and have a length of 2 or more.

    Parameters:
    string_list (list): The input list containing strings to evaluate.

    Returns:
    int: The count of strings with the same start and end character.
    """
    count = 0  # Initialize the count to 0
    
    # Iterate through each string in the list
    for string in string_list:
        # Check if the string has a length of 2 or more and if the first and last characters are the same
        if len(string) >= 2 and string[0] == string[-1]:
            count += 1  # Increment the count if conditions are met
    
    return count  # Return the count of such strings

def main():
    list = ['abc', 'xyz', 'aba', '1221', 'bb', 'a']  # Sample list of strings
    # Call the check_number_of_string_with_same_char_at_start_end function and print the result
    print("Number of strings with same start and end character:", check_number_of_string_with_same_char_at_start_end(list))

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

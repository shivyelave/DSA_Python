'''

    @Author: Shivraj Yelave
    @Date: 27-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Count Substring Occurrences in a String

'''

def count_substring_in_string(string, substring):
    """
    Description:
    Function to count the number of occurrences of a substring within a given string.

    Parameters:
    string (str): The input string to search within.
    substring (str): The substring to search for.

    Returns:
    int: The number of times the substring occurs in the input string.
    """
    count = 0  # Initialize a counter to keep track of the number of occurrences

    # Loop through the input string
    for letter in range(len(string)):
        # Check if there is enough remaining length in the string to match the substring
        if letter <= len(string) - len(substring):
            # Check if the substring matches the current position in the string
            if string[letter:letter + len(substring)] == substring:
                count += 1  # Increment the counter if a match is found

    return count  # Return the total count of substring occurrences

def main():
    string = 'abasjsbabasjkbsbabsajbsaba'  # Sample input string
    substring = 'aba'  # Substring to search for
    # Call the count_substring_in_string function and print the result
    print(f"Substring {substring} occurs {count_substring_in_string(string, substring)} times in {string}.")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

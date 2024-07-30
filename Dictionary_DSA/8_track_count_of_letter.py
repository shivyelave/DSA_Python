'''


    @Author: Shivraj Yelave
    @Date: 30-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Create and Track Word Count


'''

def create_and_track_word_count(string):

    """
    
    Description:
        Function to create a dictionary that tracks the count of each character in a given string.

    Parameters:
        string (str): The input string for which character counts are to be tracked.

    Returns:
        dict: A dictionary where keys are characters from the string, and values are their respective counts.
    
    """
    
    dictionary = {}  # Initialize an empty dictionary to store character counts
    for key in string:
        if key in dictionary:
            dictionary[key] += 1  # Increment the count if the character is found again
        else:
            dictionary[key] = 1  # Set count to 1 if the character is not found again

    return dictionary  # Return the dictionary with character counts

def main():
    # Define a sample input string
    input_string = 'shiv yelave'
    # Call the function to create and track word count and print the result
    print(create_and_track_word_count(input_string))

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

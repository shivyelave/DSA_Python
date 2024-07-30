'''
    @Author: Shivraj Yelave
    @Date: 30-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Count Length of Value Lists in Dictionary
'''

def count_length_of_value_list(dictionary):
    """
    Description:
        Function to count the length of each value list in a dictionary.

    Parameters:
        dictionary (dict): The input dictionary where each key maps to a list of values.

    Returns:
        dict: A new dictionary with the same keys, where the values are the lengths of the original value lists.
    """
    new_dictionary = {}  # Initialize an empty dictionary to store the result

    keys = dictionary.keys()  # Get all the keys from the input dictionary

    # Iterate over each key in the dictionary
    for key in keys:
        new_dictionary[key] = len(dictionary[key])  # Set the key in the new dictionary with the length of the corresponding value list
    return new_dictionary  # Return the new dictionary with lengths of value lists

def main():
    # Define a sample input dictionary with lists as values
    input_dictionary = {1: [21, 3, 42, 2, 12], 2: [28, 2, 32, 24], 3: [21, 3, 42, 2, 12], 4: []}
    # Call the function to count the lengths of value lists and print the result
    print(f"Length of each value list is: {count_length_of_value_list(input_dictionary)}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

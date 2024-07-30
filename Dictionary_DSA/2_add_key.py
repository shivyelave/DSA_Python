'''
    @Author: Shivraj Yelave
    @Date: 30-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Add Key to Dictionary
'''

def add_key(dict, new_key):
    """
    Description:
        Function to add a new key to the dictionary with a value of 30.

    Parameters:
        dict (dict): The dictionary to which the new key will be added.
        new_key (int): The new key to add to the dictionary.

    Returns:
        dict: The dictionary with the new key added.
    """
    dict[new_key] = 30  # Add the new key with a value of 30
    return dict  # Return the updated dictionary

def main():
    # Create a dictionary
    dict = {0: 10, 1: 20}
    new_key = 3  # New key to add to the dictionary

    # Print the dictionary after adding the new key
    print(f"Dictionary after adding new key: {add_key(dict, new_key)}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

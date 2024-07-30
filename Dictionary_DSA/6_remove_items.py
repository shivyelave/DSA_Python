'''
    @Author: Shivraj Yelave
    @Date: 30-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Remove Key from Dictionary
'''

def remove_key(dictionary, key):
    """
    Description:
        Function to remove a specific key from a dictionary.

    Parameters:
        dictionary (dict): The dictionary from which to remove the key.
        key (any): The key to be removed from the dictionary.

    Returns:
        dict: The dictionary after removing the specified key.
    """
    dictionary = list(dictionary.items())  # Convert dictionary items to a list of tuples
    for element in dictionary:
        if key == element[0]:  # Check if the current element's key matches the key to be removed
            dictionary.remove(element)  # Remove the key-value pair from the list
            break
    return dict(dictionary)  # Convert the list of tuples back to a dictionary

def main():
    # Define a sample dictionary
    dictionary = {'ash': 12, 'sad': 13, 'sdkj': 89, 'hsdb': 87}
    key_to_remove = 'hsdb'  # Specify the key to remove
    # Call the function to remove the key and print the result
    print(f"Dictionary after removing key {key_to_remove}: {remove_key(dictionary, key_to_remove)}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

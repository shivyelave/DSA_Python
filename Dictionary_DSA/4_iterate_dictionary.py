'''
    @Author: Shivraj Yelave
    @Date: 30-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Iterate Through Dictionary
'''

def iterate_dictionary(dictionary):
    """
    Description:
        Function to iterate through a dictionary and print each key-value pair.

    Parameters:
        dictionary (dict): The dictionary to iterate through.

    Returns:
        None
    """
    keys = dictionary.keys()  # Retrieve all keys from the dictionary
    for key in keys:
        # Print each key-value pair in the format "key:value", separated by a space
        print(f"{key}:{dictionary[key]}", end=' ')

def main():
    # Define a sample dictionary
    dictionary = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

    # Call the function to iterate through the dictionary and print key-value pairs
    iterate_dictionary(dictionary)

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

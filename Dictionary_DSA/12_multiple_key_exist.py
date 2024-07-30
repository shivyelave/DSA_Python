'''


    @Author: Shivraj Yelave
    @Date: 30-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Check Multiple Keys in Dictionary


'''

def check_keys_exist(dictionary, keys):
    """
    Description:
        Function to check if multiple keys exist in a given dictionary.

    Parameters:
        dictionary (dict): The dictionary to check for the presence of keys.
        keys (list): A list of keys to check in the dictionary.

    Returns:
        bool: True if all keys are present in the dictionary, False otherwise.
    """
    # Check if all keys are present in the dictionary
    input_keys = dictionary.keys()
    for key in keys:
        if key not in input_keys:
            return False
    else:
        return True
def main():
    # Define a sample dictionary
    sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    # Define the keys to check
    keys_to_check = ['a', 'c', 'd','g']
    
    # Call the function and print the result
    if check_keys_exist(sample_dict, keys_to_check):
        print(f"All keys {keys_to_check} exist in the dictionary.")
    else:
        print(f"Not all keys {keys_to_check} exist in the dictionary.")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

'''


    @Author: Shivraj Yelave
    @Date: 30-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Convert List to Nested Dictionary


'''

def list_to_nested_dict(input_list):
    """

    Description:
        Function to convert a list into a nested dictionary. Each key in the dictionary maps to another dictionary,
        and the last key maps to a value of 0.

    Parameters:
        input_list (list): A list of values to be used as keys and values in the nested dictionary.

    Returns:
        dict: A nested dictionary where each key maps to the next dictionary in the list.
        
    """

    if not input_list:  # If the list is empty, return an empty dictionary
        return {}

    # Initialize the dictionary with the first item as the key
    result = {input_list[0]: list_to_nested_dict(input_list[1:])}

    # If this is the last item in the list, set its value to 0
    if not input_list[1:]:
        result[input_list[0]] = 0

    return result

def main():
    # Define a sample list to convert into a nested dictionary
    sample_list = [2, 3, 4, 6, 7, 8, 9]
    # Call the function to convert the list to a nested dictionary and print the result
    print(list_to_nested_dict(sample_list))

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

'''


    @Author: Shivraj Yelave
    @Date: 30-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Concatenate Multiple Dictionaries


'''

def concatenate_dict(dict1, dict2, dict3):

    """

    Description:
        Function to concatenate three dictionaries into one.

    Parameters:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.
        dict3 (dict): The third dictionary.

    Returns:
        dict: A dictionary containing all key-value pairs from the three input dictionaries.

    """
    
    new_dict = []  # Initialize an empty list to store key-value pairs

    # Convert dictionaries to lists of tuples
    dict1 = list(dict1.items())
    dict2 = list(dict2.items())
    dict3 = list(dict3.items())

    # Append items from the first dictionary
    for index in range(len(dict1)):
        new_dict.append(dict1[index])

    # Append items from the second dictionary
    for index in range(len(dict2)):
        new_dict.append(dict2[index])        

    # Append items from the third dictionary
    for index in range(len(dict3)):
        new_dict.append(dict3[index])

    # Convert the list of tuples back to a dictionary
    return dict(new_dict)

def main():
    # Define three dictionaries
    dic1 = {1: 10, 2: 20}
    dic2 = {3: 30, 4: 40}
    dic3 = {5: 50, 6: 60}

    # Print the concatenated dictionary
    print(f"Concatenated Dictionary: {concatenate_dict(dic1, dic2, dic3)}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

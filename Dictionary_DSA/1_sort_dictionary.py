'''


    @Author: Shivraj Yelave
    @Date: 30-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Sort Dictionary


'''

def sort_dictionary(dictionary):

    """

    Description:
        Function to sort a dictionary based on its values.

    Parameters:
        dictionary (dict): The dictionary to be sorted.

    Returns:
        dict: The dictionary sorted by its values.
    
    """

    # Convert dictionary items to a list of tuples
    print(dictionary.items())
    items = list(dictionary.items())


    # Sorting logic
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i][1] > items[j][1]:  # Compare values
                items[i], items[j] = items[j], items[i]  # Swap if needed

    # Convert sorted list of tuples back to a dictionary
    sorted_dict = dict(items)
    return sorted_dict

def main():
    dictionary = {'b': 2, 'd': 4, 'a': 1, 'c': 3}  # Sample dictionary
    print(f"Sorted Dictionary: {sort_dictionary(dictionary)}")

if __name__ == '__main__':
    main()

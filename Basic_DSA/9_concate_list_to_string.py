'''


    @Author: Shivraj Yelave
    @Date: 26-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Concat list elements into string


'''

def concate(list):

    """

    Description:
    Function to concatenate list elements into a single string.

    Parameters:
    l (list): A list of elements to concatenate.

    Returns:
    str: A single string formed by concatenating the list elements.

    """
    
    string = ''  # Initialize an empty string
    for element in list:
        string += str(element)  # Convert each element to string and add it to the result
    return string

def main():

    list_input = ['S', 'h', 'i', 'v']  # Sample list of characters
    print("Concatenated string is", concate(list_input))  # Call the concate function and print the result

if __name__ == '__main__':
    main()  # Execute the main function if the script is run directly

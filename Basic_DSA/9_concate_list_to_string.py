'''


    @Author: Shivraj Yelave
    @Date: 26-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Concat list elements into string


'''

def concate(l):

    """

    Description:
    Function to concatenate list elements into a single string.

    Parameters:
    l (list): A list of elements to concatenate.

    Returns:
    str: A single string formed by concatenating the list elements.

    """
    
    s = ''  # Initialize an empty string
    for i in l:
        s += str(i)  # Convert each element to string and add it to the result
    return s

def main():

    l = ['S', 'h', 'i', 'v']  # Sample list of characters
    print("Concatenated string is", concate(l))  # Call the concate function and print the result

if __name__ == '__main__':
    main()  # Execute the main function if the script is run directly

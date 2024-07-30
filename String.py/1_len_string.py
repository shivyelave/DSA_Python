'''

    @Author: Shivraj Yelave
    @Date: 26-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Calculate the Length of a String

'''

def length(string):
    """
    Description:
    Function to calculate the length of a string.

    Parameters:
    s (str): The string whose length is to be calculated.

    Returns:
    int: The length of the string.
    """
    count = 0  # Initialize the count to 0
    for _ in string:
        count += 1  # Increment the count for each character in the string
    return count

def main():
    string = input("Enter string: ")  # Prompt the user to enter a string
    print("Length is", length(string))  # Call the length function and print the result

if __name__ == '__main__':
    main()  # Execute the main function if the script is run directly

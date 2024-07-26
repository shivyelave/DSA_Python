'''


    @Author: Shivraj Yelave
    @Date: 25-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Check Number in List

    
'''

def check_in_list(lst, number):
    '''
    Description:
        This function checks if a specific number is present in a given list.

    Parameters:
        lst : list : the list in which to check for the number.
        number : int : the number to check for in the list.

    Returns:
        bool : True if the number is present in the list, otherwise False.
    '''
    return number in lst

def main():
    # Define a list and the number to check
    lst = [1, 5, 8, 3]
    number = 9
    
    # Check if the number is in the list and print the result
    if check_in_list(lst, number):
        print(f"{number} is present in the list {lst}.")
    else:
        print(f"{number} is not present in the list {lst}.")

if __name__ == '__main__':
    # Call the main function when the script is executed
    main()

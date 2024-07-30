'''

    @Author: Shivraj Yelave
    @Date: 25-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: User name

'''
def reverse_name(user_name):
    """
        Description:
        capitalize the first letter and return name in reverse order.

        Parameters:
        user_name : user name.

        Returns:
        name in reverse order
    """
    
    name = user_name.split(' ')
    
    # Print the user's name in the format "LastName FirstName"
    # Convert the first character of each name to uppercase and concatenate it with the rest of the name
    return f"Hello, {name[1][0].upper()}{name[1][1:]} {name[0][0].upper()}{name[0][1:]}"
def main():
    # Prompt the user to enter their first and last name
    user_name = input("Enter your first name and last name: ")
    
    # Split the user input into a list where the first element is the first name and the second element is the last name
    print(reverse_name(user_name))

if __name__ == '__main__':
    # Call the main function when the script is executed
    main()

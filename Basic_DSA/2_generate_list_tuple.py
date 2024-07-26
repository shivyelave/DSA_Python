'''

    @Author: Shivraj Yelave
    @Date: 25-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Convert to list and tuple

'''

def main():
    # Prompt the user to enter numbers separated by commas
    numbers = input("Enter numbers separated by commas: ")
    
    # Split the input string by commas to create a list of numbers
    num_list = numbers.split(',')
    
    # Print the list
    print("List:", num_list)
    
    # Convert the list to a tuple and print the tuple
    print("Tuple:", tuple(num_list))

if __name__ == '__main__':
    # Call the main function when the script is executed
    main()

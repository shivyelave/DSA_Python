'''

    @Author: Shivraj Yelave
    @Date: 27-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Sort Unique Colors Alphabetically by First Letter

'''

def unique_sort(colors):
    """
    Description:
    Function to sort and return unique color names alphabetically by their first letter.

    Parameters:
    colors (list): The input list of color names.

    Returns:
    str: A string representation of the set of sorted unique color names.
    """
    sorted_list = []  # Initialize an empty list to hold the sorted colors

    # Loop through ASCII values of 'a' to 'z'
    for i in range(ord('a'), ord('z') + 1):
        # Loop through each color in the input list
        for color in colors:
            # If the first letter of the color (in lowercase) matches the current character
            if chr(i) == color[0].lower():
                # Add the color to the sorted list
                sorted_list.append(color)
    
    # Convert the sorted list to a set to remove duplicates, then convert back to a list for sorting
    unique_sorted_list = sorted(set(sorted_list))
    
    # Return the unique sorted list as a string
    return str(unique_sorted_list)

def main():
    colors = ['red', 'white', 'black', 'red', 'green', 'black']  # Sample list of colors
    # Call the unique_sort function with the sample list and print the result
    print("Unique Words:", unique_sort(colors))

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

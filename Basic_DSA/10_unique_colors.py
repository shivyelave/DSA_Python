'''

    @Author: Shivraj Yelave
    @Date: 26-02-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Find Unique Colors from Two Lists

'''

def unique_colors(l1, l2):
    """
    Description:
    Function to find unique colors from the first list that are not in the second list.

    Parameters:
    l1 (set): The first set of colors.
    l2 (set): The second set of colors.

    Returns:
    set: A set of unique colors from the first list.
    """
    unique = {color for color in l1 if color not in l2}  # Create a set of unique colors
    return unique

def main():
    color_list_1 = set(["White", "Black", "Red"])  # First set of colors
    color_list_2 = set(["Red", "Green"])  # Second set of colors

    # Call the unique_colors function and print the result
    print("Unique color set is", unique_colors(color_list_1, color_list_2))

if __name__ == '__main__':
    main()  # Execute the main function if the script is run directly

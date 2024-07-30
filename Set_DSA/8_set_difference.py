'''

    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Set Difference

'''

def set_difference(set1, set2):
    """
    Description:
    Function to compute the difference between two sets. Elements present in either set but not in both.

    Parameters:
    set1 (set): The first set.
    set2 (set): The second set.

    Returns:
    set: A set containing elements that are in either set1 or set2 but not in both.
    """
    difference = set()  # Initialize an empty set to store the difference

    # Add elements from set1 that are not in set2
    for element in set1:
        if element not in set2:
            difference.add(element)

    # Add elements from set2 that are not in set1
    for element in set2:
        if element not in set1:
            difference.add(element)

    return difference  # Return the set containing the difference

def main():
    set1 = {1, 2, 3, 4, 5}  # Sample set1
    set2 = {4, 5, 6, 7, 8}  # Sample set2
    print(f"Difference of set {set1} and {set2}: {set_difference(set1, set2)}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

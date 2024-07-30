'''

    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Intersection of Two Sets

'''

def intersection_set(set1, set2):
    """
    Description:
    Function to find the intersection of two sets.

    Parameters:
    set1 (set): The first set.
    set2 (set): The second set.

    Returns:
    set: The intersection of set1 and set2.
    """
    common_elements = set()
    for item in set1:
        if item in set2:
            common_elements.add(item)
    return common_elements

def main():
    set1 = {1, 2, 3, 4, 5}  # Sample set1
    set2 = {4, 5, 6, 7, 8}  # Sample set2
    print(f"Intersection of set {set1} and {set2}: {intersection_set(set1, set2)}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

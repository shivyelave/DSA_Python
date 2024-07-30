'''

    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Union of Two Sets

'''

def union_set(set1, set2):
    """
    Description:
    Function to find the union of two sets.

    Parameters:
    set1 (set): The first set.
    set2 (set): The second set.

    Returns:
    set: The union of set1 and set2.

    """
    # Add elements from set1
    union_set= set()
    for element in set1:
        if element not in union_set:
            union_set.add(element)

    # Add elements from set2
    for element in set2:
        if element not in union_set:
            union_set.add(element)
    return union_set  # Use the union operator to find the union of the sets

def main():
    set1 = {1, 2, 3, 4, 5}  # Sample set1
    set2 = {4, 5, 6, 7, 8}  # Sample set2
    print(f"Union of set {set1} and {set2}: {union_set(set1, set2)}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

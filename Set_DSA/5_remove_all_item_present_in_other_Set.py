'''

    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Remove Items Present in Another Set

'''

def remove_all_item_present_in_other_set(set1, set2):
    """
    Description:
    Function to remove all items from set1 that are present in set2.

    Parameters:
    set1 (set): The set from which items will be removed.
    set2 (set): The set containing items to be removed from set1.

    Returns:
    set: The updated set1 after removing items present in set2.
    """
    temp = set()
    for item in set1:
        if item in set2:
            temp.add(item)
    for item in temp:
        set1.remove(item)
    return set1

def main():
    set1 = {1, 2, 3, 4, 5}  # Sample set1
    set2 = {4, 5, 6, 7, 8}  # Sample set2
    print(f"Set {set1} after removing elements present in set {set2}: {remove_all_item_present_in_other_set(set1, set2)}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

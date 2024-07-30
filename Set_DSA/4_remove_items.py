'''

    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Remove Item from a Set

'''

def remove_item(input_set, item):
    """
    Description:
    Function to remove an item from a set.

    Parameters:
    input_set (set): The set from which the item will be removed.
    item: The item to be removed from the set.

    Returns:
    set: The updated set after removing the item.
    """
    # Remove the item from the set if it exists
    input_set.discard(item)  # `discard` does not raise an error if the item is not found
    return input_set  # Return the updated set

def main():
    input_set = {2, 3, 4, 5, 6}  # Sample input set
    item_to_remove = 4  # Item to be removed
    print(f"Set {input_set} after removing {item_to_remove}: {remove_item(input_set, item_to_remove)}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

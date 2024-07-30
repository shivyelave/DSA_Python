'''

    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Symmetric Difference of Two Sets

'''

def symmetric_difference(set1, set2):
    '''
    Description:
        This function returns the symmetric difference between two sets.

    Parameters:
        set1 : set : the first set.
        set2 : set : the second set.

    Returns:
        set : the symmetric difference between the two sets.
    '''
    # Calculate the symmetric difference between set1 and set2
    sym_diff = set1.symmetric_difference(set2)
    return sym_diff

def main():
    set1 = {1, 2, 3, 4, 5}  # Sample set1
    set2 = {4, 5, 6, 7, 8}  # Sample set2
    # Print the symmetric difference of set1 and set2
    print(f"Symmetric difference of set {set1} and {set2}: {symmetric_difference(set1, set2)}")

# If this script is run as the main module, execute the main function
if __name__ == '__main__':
    main()

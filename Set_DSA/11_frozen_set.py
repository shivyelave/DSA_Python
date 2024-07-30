'''

    @Author: Shivraj Yelave
    @Date: 29-07-24
    @Last modified by: Shivraj Yelave
    @Last modified time:
    @Title: Operations with Frozensets

'''

def frozenset_operations():
    """
    Description:
    Function to demonstrate various operations with frozensets.

    Returns:
    None
    """
    # Creating frozensets
    frozenset1 = frozenset([1, 2, 3, 4, 5])
    frozenset2 = frozenset([4, 5, 6, 7, 8])

    # Display the frozensets
    print("Frozenset 1:", frozenset1)
    print("Frozenset 2:", frozenset2)

    # Performing operations on frozensets

    # Union of frozensets
    union_result = frozenset1 | frozenset2
    print("Union:", union_result)

    # Intersection of frozensets
    intersection_result = frozenset1 & frozenset2
    print("Intersection:", intersection_result)

    # Difference of frozensets
    difference_result = frozenset1 - frozenset2
    print("Difference:", difference_result)


def main():
    frozenset_operations()

if __name__ == '__main__':
    main()
